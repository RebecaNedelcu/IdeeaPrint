import { ApiUser } from "../models/User";

export interface LoginResponse {
  access_token: string;
  refresh_token: string;
  user: ApiUser;
  access_token_lifetime: number;
}
