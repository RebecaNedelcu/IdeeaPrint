import { Cookies } from "quasar";
import { reactive } from "vue";
import { ApiUser } from "./models/User";
import { LoginResponse, RegisterResponse } from "./types/ApiResponses";
import { addMinutes, setAccessToken, setExpiresAt } from "./useAccessToken";
import { useApi } from "./useApi";
import { setRefreshToken } from "./useRefreshToken";

interface StateType {
  user: {
    email: string;
    password: string;
    firstName: string;
    lastName: string;
    isLoggedIn: boolean;
    favoriteProducts: number[];
  };
}

const state = reactive<StateType>({
  user: {
    email: "",
    password: "",
    firstName: "",
    lastName: "",
    isLoggedIn: false,
    favoriteProducts: [1],
  },
});

export const useUser = () => {
  const isProductFavorite = (productId: number) => {
    return state.user.favoriteProducts.includes(productId);
  };

  const setUser = (user: ApiUser | undefined) => {
    if (user) {
      state.user.email = user.email;
      state.user.firstName = user.first_name;
      state.user.lastName = user.last_name;
      state.user.isLoggedIn = true;
    } else {
      state.user.email = "";
      state.user.firstName = "";
      state.user.lastName = "";
      state.user.isLoggedIn = false;
    }
  };

  const login = async (email: string, password: string) => {
    try {
      let { data, error, ok } = await useApi<LoginResponse>({
        url: "login/",
        method: "POST",
        body: {
          email: email,
          password: password,
        },
        publicRoute: true,
      });
      if (!ok) {
        return { error: error.detail };
      } else {
        if (data) {
          setAccessToken(data.access_token);
          setExpiresAt(addMinutes(data.access_token_lifetime));
          setUser(data.user);

          if (data.refresh_token) {
            setRefreshToken(data.refresh_token);
          }
          Cookies.set("access_token", data.access_token);
        }
      }
    } catch (error) {
      console.log("Login err: ", error);
    }
    return { error: "" };
  };

  const register = async (
    email: string,
    password: string,
    firstName: string,
    lastName: string
  ) => {
    try {
      let { data, error, ok } = await useApi<RegisterResponse>({
        url: "register/",
        method: "POST",
        body: {
          email: email,
          username: email,
          password: password,
          first_name: firstName,
          last_name: lastName,
        },
        publicRoute: true,
      });
      if (!ok) {
        return { error: error.detail };
      } else {
        if (data) {
          console.log(data);
          setUser(data);
        }
      }
    } catch (error) {
      console.log("Login err: ", error);
    }
    return { error: "" };
  };

  const logout = () => {
    Cookies.remove("access_token");
    setUser(undefined);
  };

  const getUserDetails = async () => {
    try {
      const { data, error } = await useApi<ApiUser>({ url: "get_user" });
      if (error.detail === "") setUser(data);
    } catch (error) {
      console.log(error);
    }
  };

  const toggleFavoriteProduct = (productId: number) => {
    if (isProductFavorite(productId)) {
      state.user.favoriteProducts = state.user.favoriteProducts.filter(
        (id) => id !== productId
      );
    } else {
      state.user.favoriteProducts.push(productId);
    }
  };

  return {
    isProductFavorite,
    login,
    state,
    register,
    logout,
    getUserDetails,
    toggleFavoriteProduct,
  };
};
