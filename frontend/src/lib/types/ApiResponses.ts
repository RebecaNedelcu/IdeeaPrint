import { ApiUser } from "../models/User";

export interface LoginResponse {
  access_token: string;
  refresh_token: string;
  user: ApiUser;
  access_token_lifetime: number;
}

export interface RegisterResponse {
  email: string;
  first_name: string;
  id: number;
  is_active: boolean;
  is_staff: boolean;
  last_name: string;
  username: string;
}
