import { Notify } from "quasar";

type NotificationType =
  | "positive"
  | "negative"
  | "warning"
  | "info"
  | "ongoing";

interface notificationInterface {
  type: NotificationType;
  message: string;
  timeout?: number;
  handler?: () => void;
}

export const showToast = async ({
  type,
  message,
  timeout = 3000,
  handler = () => {},
}: notificationInterface) => {
  Notify.create({
    type,
    message,
    progress: true,
    // multiLine: true,
    timeout,
    actions: [
      {
        label: "Dismiss",
        color: "white",
        handler,
      },
    ],
  });
};
