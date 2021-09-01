export interface ApiUser {
  id: number;
  username: string;
  email: string;
  is_staff: boolean;
  is_active: boolean;
  first_name: string;
  last_name: string;
}

export interface ApiUserDetails {
  city: string;
  company: string;
  country: string;
  county: string;
  street: string;
  phone: string;
  zipcode: string;
  user: ApiUser;
}
