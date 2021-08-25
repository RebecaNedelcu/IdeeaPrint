import { ApiUser } from './models/User';
import { reactive } from "vue";
import { LoginResponse } from "./types/ApiResponses";
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

  const setUser = (user: ApiUser) => {
    console.log(user);

    state.user.email = user.email;
    state.user.firstName = user.first_name;
    state.user.lastName = user.last_name;
    state.user.isLoggedIn = true;
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
        }
      }
    } catch (error) {
      console.log("Login err: ", error);
    }
    return { error: "" };
  };

  return { isProductFavorite, login, state };
};
