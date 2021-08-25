import { LoginResponse } from './types/ApiResponses';
import { addMinutes, setAccessToken, setExpiresAt } from "./useAccessToken";
import { Cookies } from "quasar";
import { useApi } from "./useApi";

export const setRefreshToken = (refresh_token: string) => {
  Cookies.set("refresh_token", refresh_token, {
    expires: "7d"
  });
};

export const deleteRefreshToken = () => {
  Cookies.remove("refresh_token");
};

export const getAccessTokenFromRT = async () => {
  // TODO change this to correct type
  let { data, error, ok } = await useApi<LoginResponse>({
    url: "auth/refresh_token/",
    method: "POST",
    publicRoute: true
  });

  if (!ok) {
    deleteRefreshToken();
    setAccessToken("");

    return false;
  } else {
    setAccessToken(data.access_token);
    setExpiresAt(addMinutes(data.access_token_lifetime));
    // setStaticUser(data.user);

    if (data.refresh_token) {
      setRefreshToken(data.refresh_token);
    }

    return true;
  }
};
