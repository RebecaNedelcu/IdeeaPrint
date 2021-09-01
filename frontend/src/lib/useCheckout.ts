import { ProductDetails } from "./types/ApiResponses";
import { CartProduct } from "./models/CartProduct";
import { showToast } from "./useToast";
import { Order, OrderApi } from "./models/Order";
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
    const { data, error, ok } = await useApi<OrderApi>({
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

    return { data, error, ok };
  };

  const sendProducts = async (product: CartProduct, orderId: number) => {
    const { data: detailsData } = await useApi<ProductDetails>({
      url: `shop/get_product_details_for_cart/${product.productId}/${product.selectedSize}`,
    });
    await useApi<CartProduct>({
      url: "shop/order_products/",
      method: "POST",
      body: {
        order: orderId,
        product: detailsData.id,
        quantity: product.quantity,
        price: product.price,
        illustration: product.illustrationId,
        llustration_from_user: product.editorIllustration,
      },
    });
  };

  return { makeOrder, sendProducts };
};
