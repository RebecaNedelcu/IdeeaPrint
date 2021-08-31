import { ApiUser } from "./User";

export interface Illustration {
  id: number;
  image: string;
  name: string;
  created_at: string;
}

export interface FavoriteIllustrations {
  id: number;
  user: ApiUser;
  illustration: Illustration;
}
