export interface Order {
  firstName: string;
  lastName: string;
  phone: string;
  company: string;
  street: string;
  city: string;
  zipcode: string;
  county: string;
  country: string;
  paymentType: string;
  status: string;
  delivery_date?: string;
}

export interface OrderApi {
  id: number;
  firstName: string;
  lastName: string;
  phone: string;
  company: string;
  street: string;
  city: string;
  zipcode: string;
  county: string;
  country: string;
  paymentType: string;
  status: string;
}
