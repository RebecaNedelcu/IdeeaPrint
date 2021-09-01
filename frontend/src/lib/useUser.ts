import { Cookies } from "quasar";
import { reactive } from "vue";
import { FavoriteIllustrations } from "./models/Illustration";
import { ApiUser, ApiUserDetails } from "./models/User";
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
    favoriteIllustrations: number[];
    city?: string;
    company?: string;
    country?: string;
    county?: string;
    phone?: string;
    street?: string;
    zipcode?: string;
  };
}

const state = reactive<StateType>({
  user: {
    email: "",
    password: "",
    firstName: "",
    lastName: "",
    isLoggedIn: false,
    favoriteIllustrations: [],
    city: "",
    company: "",
    country: "",
    county: "",
    phone: "",
    street: "",
    zipcode: "",
  },
});

export const useUser = () => {
  const isIllustrationFavorite = (illustrationId: number) => {
    return state.user.favoriteIllustrations.includes(illustrationId);
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
      state.user.favoriteIllustrations = [];
    }
  };

  const setUserWithDetails = (data: ApiUserDetails | undefined) => {
    if (data) {
      state.user.email = data.user.email;
      state.user.firstName = data.user.first_name;
      state.user.lastName = data.user.last_name;
      state.user.isLoggedIn = true;
      state.user.city = data.city;
      state.user.company = data.company;
      state.user.country = data.country;
      state.user.county = data.county;
      state.user.zipcode = data.zipcode;
      state.user.phone = data.phone;
      state.user.street = data.street;
    }
  };

  const getFavoriteIllustrations = async () => {
    try {
      const { data } = await useApi<FavoriteIllustrations[]>({
        url: "shop/get_favorite",
      });

      data.forEach((il) => {
        state.user.favoriteIllustrations.push(il.illustration.id);
      });
    } catch (error) {
      console.log(error);
    }
  };

  const getFavoriteIllustrationsWithData = async () => {
    try {
      const { data } = await useApi<FavoriteIllustrations[]>({
        url: "shop/get_favorite",
      });
      return data;
    } catch (error) {
      console.log(error);
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
          await getFavoriteIllustrations();
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
      const { data } = await useApi<ApiUserDetails>({
        url: "get_user_details",
      });
      setUserWithDetails(data);
      await getFavoriteIllustrations();
    } catch (error) {
      console.log(error);
    }
  };

  const toggleFavoriteIllustrations = async (illustrationId: number) => {
    try {
      await useApi({
        url: `shop/toggle_favorite/${illustrationId}`,
        method: "POST",
      });

      if (isIllustrationFavorite(illustrationId)) {
        state.user.favoriteIllustrations =
          state.user.favoriteIllustrations.filter(
            (id) => id !== illustrationId
          );
      } else {
        state.user.favoriteIllustrations.push(illustrationId);
      }
    } catch (error) {
      console.log(error);
    }
  };

  return {
    isIllustrationFavorite,
    login,
    state,
    register,
    logout,
    getUserDetails,
    toggleFavoriteIllustrations,
    getFavoriteIllustrationsWithData,
  };
};
