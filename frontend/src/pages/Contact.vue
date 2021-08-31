<template>
  <q-page class="contactPage justify-center items-center">
    <div class="contactContainer row justify-center items-center">
      <div class="inputContact col">
        <p class="text-h2 text-bold">Contact US</p>
        <span class="text-subtitle1 text-weight-bold"
          >Feel free to contact us any time. We will get back to you as soon as
          we can!
        </span>
        <q-input
          square
          standout="bg-grey-3"
          v-model="name"
          placeholder="Name"
          class="messageInput q-my-md"
          :input-style="{ color: '#000000' }"
        />
        <q-input
          square
          standout="bg-grey-3"
          v-model="email"
          placeholder="Email"
          class="messageInput q-my-md"
          :input-style="{ color: '#000000' }"
        />
        <q-input
          v-model="message"
          autogrow
          square
          standout="bg-grey-3"
          placeholder="Message"
          class="messageInput q-my-md"
          :input-style="{ color: '#000000' }"
        />
        <q-btn
          no-caps
          flat
          color="black"
          label="SEND"
          class="
            no-border-radius
            brdrButtons
            text-bold text-h6
            column
            bttns-home
            marginBtn
            q-my-md
          "
          @click="onSendClick"
        />
      </div>

      <div class="infoDiv col q-pa-lg q-py-xl">
        <p class="text-h4 text-bold">Info</p>
        <q-list bordered>
          <q-item class="q-py-lg">
            <q-item-section avatar>
              <q-icon color="primary" name="mail_outline" />
            </q-item-section>

            <q-item-section class="text-h6"
              >office@ideeaprint.ro</q-item-section
            >
          </q-item>
          <q-item class="q-py-lg">
            <q-item-section avatar>
              <q-icon color="primary" name="fas fa-mobile-alt" />
            </q-item-section>

            <q-item-section class="text-h6">+40 729 732 352</q-item-section>
          </q-item>
          <q-item
            class="q-py-lg"
            clickable
            v-ripple
            tag="a"
            href="https://goo.gl/maps/MpzsHCsK91rXgX1o9"
            target="_blank"
          >
            <q-item-section avatar>
              <q-icon color="primary" name="place" />
            </q-item-section>

            <q-item-section class="text-h6"
              >Str. Constantin Brancoveanu, nr.19</q-item-section
            >
          </q-item>
          <q-item class="q-py-lg">
            <q-item-section avatar>
              <q-icon color="primary" name="schedule" />
            </q-item-section>

            <q-item-section class="text-h6">9:00 - 18:30</q-item-section>
          </q-item>
        </q-list>
      </div>
    </div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useContactMessage } from "../lib/useContactMessage";
import { showToast } from "../lib/useToast";

export default defineComponent({
  name: "PageContact",
  components: {},
  setup() {
    let name = ref("");
    let email = ref("");
    let message = ref("");

    const { sendContactMessage } = useContactMessage();
    const onSendClick = async () => {
      if (name.value !== "" && email.value !== "" && message.value !=="") {
        try {
          const { error } = await sendContactMessage(
            name.value,
            email.value,
            message.value
          );
          if (error) {
            showToast({ type: "negative", message: error });
            return;
          }
          showToast({ type: "positive", message: "Message sent!" });
          name.value=""
          email.value=""
          message.value=""
        } catch (error) {
          showToast({ type: "negative", message: error });
        }
      } else {
          showToast({ type: "negative", message: "Câmp gol!" });
      }
    };

    return {
      name,
      email,
      message,
      onSendClick,
    };
  },
});
</script>

<style lang="scss" scoped>
.contactPage {
  font-family: raleway;
  background-image: linear-gradient(90deg, white 85%, $info 15%);
  height: 85vh;
}
.contactContainer {
  height: 100%;
}
.messageInput {
  border-style: solid;
  border-width: 2px;
  font-family: raleway;
  max-width: 19em;
}
.brdrButtons {
  border-style: solid;
  background-color: #c6b9ff;
  border-width: 6px;
  width: 20em;

  font-family: raleway;
}
.infoDiv {
  background-color: black;
  color: white;
  margin-left: 25%;
}
.inputContact {
  margin-left: 10%;
}
</style>