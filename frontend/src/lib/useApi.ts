import { Cookies } from "quasar";

const BASE_URL = "http://localhost:8000/api/";

interface apiInterface {
  url: RequestInfo;
  method?: string;
  body?: object;
  publicRoute?: boolean;
}

export async function useApi<T>({
  url,
  method = "GET",
  body = {},
  publicRoute = false,
}: apiInterface): Promise<{ data: T; error: { detail: string }; ok: boolean }> {
  const apiResponse = {
    error: { detail: "" },
    data: {} as T,
    ok: Boolean(),
  };

  let canDo = true;

  //   if (!publicRoute) {
  //     if (getExpiresAt() < new Date()) {
  //       canDo = await getAccessTokenFromRT();
  //     }
  //   }

  if (canDo) {
    let options: RequestInit = {
      method: method,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${Cookies.get('access_token')}`,
        "X-CSRFToken": Cookies.get("csrftoken"),
      },
      credentials: "include",
    };

    if (method !== "GET") {
      options.body = JSON.stringify(body);
    }

    try {
      const response = await fetch(`${BASE_URL + url}`, options).catch(
        (err) => {
          console.log("fetch: ", err);
        }
      );

      if (response) {
        apiResponse.ok = response.ok;
        if (response.ok) {
          apiResponse.data = await response.json();
        } else {
          apiResponse.error = await response.json();
        }
      }
    } catch (error) {
      console.log("fetch err: ", error);
    }
  }

  return {
    data: apiResponse.data,
    error: apiResponse.error,
    ok: apiResponse.ok,
  };
}
