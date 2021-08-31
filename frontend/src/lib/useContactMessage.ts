import { useApi } from "./useApi";
import { ContactMessage } from './models/ContactMessage';

export const useContactMessage = () => {

    const sendContactMessage = async (name: string, email: string, message: string) => {
      try {
        let { data, error, ok } = await useApi<ContactMessage>({
          url: "shop/sendcontactmessage/",
          method: "POST",
          body: {
            name: name,
            email: email,
            message: message,
          },
          publicRoute: true,
        });
        if (!ok) {
          return { error: error.detail };
        } else {
          if (data) {
           console.log(data)
          }
        }
      } catch (error) {
        console.log("Message error: ", error);
      }
      return { error: "" };
    };
  
    return { sendContactMessage };
  };
  