import { showToast } from "./useToast";
import { Order } from "./models/Order";
import { useApi } from "./useApi";

export const useCheckout = () => {
  const makeOrder = async ({
    firstName,
    lastName,
    phone,
    company,
    street,
    city,
    zipcode,
    county,
    country,
    paymentType,
  }: Order) => {
    const { data, error, ok } = await useApi({
      url: "shop/order/",
      method: "POST",
      body: {
        first_name: firstName,
        last_name: lastName,
        phone,
        company,
        street,
        city,
        zipcode,
        county,
        country,
        payment_type: paymentType,
      },
    });

    if (ok && error.detail === "") {
      showToast({ message: "Comanda plasata", type: "positive" });
    }
  };

  return { makeOrder };
};
