<template>
  <q-layout view="hHr lpR ffr">
    <q-header class="bg-primary text-secondary" height-hint="98">
      <q-toolbar>
        <q-toolbar-title class="text-bold text-h3 logo">
          ideeaprint
        </q-toolbar-title>
        <q-tabs
          narrow-indicator
          no-caps
          align="left"
          inline-label
          class="text-weight-bold text-h6 q-mr-xl"
        >
          <q-route-tab to="/" class="q-px-md" exact> home </q-route-tab>

          <q-btn-dropdown
            no-caps
            auto-close
            flat
            label="shop"
            dropdown-icon="fas fa-caret-down"
            class="text-weight-bold text-h6 q-px-md"
          >
            <q-list class="items text-bold">
              <q-item
                clickable
                to="/shop/1"
                active-class="shop-dropdown-button-active"
              >
                <q-item-section>t-shirts</q-item-section>
              </q-item>
              <q-item
                clickable
                to="/shop/2"
                active-class="shop-dropdown-button-active"
              >
                <q-item-section>hoodies</q-item-section>
              </q-item>
              <q-item
                clickable
                to="/shop/3"
                active-class="shop-dropdown-button-active"
              >
                <q-item-section>mugs</q-item-section>
              </q-item>
              <q-item
                clickable
                to="/shop/4"
                active-class="shop-dropdown-button-active"
              >
                <q-item-section>totebags</q-item-section>
              </q-item>
            </q-list>
          </q-btn-dropdown>

          <q-route-tab to="/design" class="q-px-xs" exact> design </q-route-tab>
          <q-route-tab to="/contact" class="q-px-xs" exact>
            contact
          </q-route-tab>
        </q-tabs>
        <q-btn
          dense
          flat
          round
          icon="far fa-heart"
          class="q-mx-sm"
          @click="$router.push('/favorite')"
        />

        <q-btn-dropdown no-caps auto-close flat dropdown-icon="far fa-user">
          <q-list class="items">
            <q-item>
              <q-item-section class="text-secondary non-selectable">
                {{
                  userState.user.isLoggedIn
                    ? `${userState.user.firstName} ${userState.user.lastName}`
                    : "You're not logged in"
                }}
              </q-item-section>
            </q-item>
            <q-separator />
            <div v-if="!userState.user.isLoggedIn">
              <q-item
                clickable
                @click="tab = 'sign in'"
                to="/signin"
                class="text-bold"
              >
                <q-item-section>sign in</q-item-section>
              </q-item>
              <q-item
                clickable
                @click="tab = 'signup'"
                to="/signup"
                class="text-bold"
              >
                <q-item-section>sign up</q-item-section>
              </q-item>
            </div>
            <div v-else>
              <q-item clickable @click="logout" class="text-bold">
                <q-item-section>logout</q-item-section>
              </q-item>
            </div>
          </q-list>
        </q-btn-dropdown>

        <q-btn
          dense
          flat
          round
          icon="fas fa-shopping-bag"
          @click="toggleRightDrawer"
          class="q-ml-sm q-mr-xl"
        >
          <q-badge color="black" floating rounded
            >{{ cartState.cartProducts.length }}
          </q-badge>
        </q-btn>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="rightDrawerOpen" side="right" bordered>
      <q-scroll-area style="height: calc(100% - 300px); margin-bottom: 300px">
        <q-list separator bordered>
          <cart-item-component
            v-for="product in cartState.cartProducts"
            :cartProduct="product"
            :key="product.id"
          />
        </q-list>
      </q-scroll-area>

      <div
        class="
          column
          item-design
          text-bold
          q-gutter-y-sm
          text-body1
          q-pr-md q-pl-sm
          absolute-bottom
        "
      >
        <div class="row justify-between">
          <span>SUBTOTAL</span>
          <span>{{ subtotal }} LEI</span>
        </div>
        <div class="row justify-between">
          <span>DELIVERY</span>
          <span>{{ delivery }} LEI</span>
        </div>
        <div class="row justify-between">
          <span>DISCOUNT</span>
          <span>-{{ discount }} LEI</span>
        </div>
        <div class="q-px-lg">
          <q-input
            clearable
            dense
            v-model="discountCode"
            color="accent"
            placeholder="Add discount"
          />
        </div>
        <div class="row justify-between text-h6 text-bold q-py-sm">
          <span>TOTAL</span>
          <span>{{ total }} LEI</span>
        </div>
        <div class="row q-mb-lg">
          <q-btn
            flat
            color="black"
            label="APPLY DISCOUNT"
            push
            size="md"
            v-close-popup
            class="no-border-radius discountButton text-bold q-px-lg col"
            @click="applyDiscount"
          />
          <q-btn
            flat
            color="black"
            label="CHECKOUT"
            push
            size="md"
            v-close-popup
            class="no-border-radius checkoutButton text-bold q-px-lg col"
            to="/checkout"
          />
        </div>
      </div>
    </q-drawer>

    <q-page-container>
      <router-view> </router-view>
    </q-page-container>

    <q-footer class="text-black">
      <q-toolbar class="row justify-center">
        <q-btn
          dense
          flat
          round
          icon="fab fa-facebook"
          class="q-mx-sm"
          type="a"
          href="https://www.facebook.com/avigeoprint"
          target="_blank"
        />
        <q-btn
          dense
          flat
          round
          icon="fab fa-instagram"
          class="q-mx-sm"
          type="a"
          href="https://www.instagram.com/ideeaprint/"
          target="_blank"
        />
        <q-btn
          dense
          flat
          round
          icon="fab fa-youtube"
          class="q-mx-sm"
          type="a"
          href="https://www.youtube.com/channel/UCeKKhW5LVMXV2-D9isTiWgA"
          target="_blank"
        />
        <q-btn
          dense
          flat
          round
          icon="fab fa-linkedin-in"
          class="q-mx-sm"
          type="a"
          href="https://www.linkedin.com/in/rebeca-nedelcu-0a156a182"
          target="_blank"
        />
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script lang="ts">
import { Cookies } from "quasar";
import { defineComponent, ref, onMounted, watch } from "vue";
import CartItemComponent from "../components/CartItemComponent.vue";
import { CartProduct } from "../lib/models/CartProduct";
import { useCart } from "../lib/useCart";
import { useUser } from "../lib/useUser";

export default defineComponent({
  name: "MainLayout",

  components: { CartItemComponent },

  setup() {
    const { state: userState, getUserDetails, logout } = useUser();
    const { state: cartState } = useCart();
    const rightDrawerOpen = ref(false);
    const discountCode = ref("");

    let subtotal = ref(0);
    let total = ref(0);
    let delivery = ref(25);

    let isDiscountApplied = ref(false);
    let discount = ref(0);

    const updateProductsSummary = () => {
      subtotal.value = 0;
      cartState.cartProducts.forEach((cartProduct) => {
        subtotal.value += cartProduct.quantity * parseInt(cartProduct.price);
      });
      if (isDiscountApplied.value) {
        discount.value = (subtotal.value * 30) / 100;
        subtotal.value -= discount.value;
      }
      if (subtotal.value > 299) {
        delivery.value = 0;
      } else {
        delivery.value = 25;
      }
      if (subtotal.value > 0) {
        total.value = subtotal.value + delivery.value;
      } else {
        total.value = 0;
      }
      if (cartState.cartProducts.length === 0) {
        total.value = 0;
      }
    };
    watch(cartState.cartProducts, updateProductsSummary);

    const applyDiscount = () => {
      if (!isDiscountApplied.value) {
        {
          if (discountCode.value === "ideeaprint30") {
            isDiscountApplied.value = true;
            updateProductsSummary();
          }
        }
      }
    };
    onMounted(async () => {
      if (Cookies.has("access_token")) {
        await getUserDetails();
      }
      updateProductsSummary();
    });

    return {
      CartItemComponent,
      cartState,
      discountCode,
      rightDrawerOpen,
      userState,
      logout,
      toggleRightDrawer() {
        rightDrawerOpen.value = !rightDrawerOpen.value;
      },
      subtotal,
      total,
      delivery,
      applyDiscount,
      discount,
    };
  },
});
</script>

<style lang="scss" scoped>
.logo {
  font-family: raleway;
  margin-left: 5%;
}
.items {
  font-family: raleway;
}
.item-design {
  font-family: raleway;
}
.deleteBtn {
  border-style: solid;
  border-width: 2px;
  background-color: white;
}
.checkoutButton {
  border-style: solid;
  background-color: #c6b9ff;
  border-width: 3px;
}
.discountButton {
  border-style: solid;
  background-color: $info;
  border-width: 3px;
}
.shop-dropdown-button-active {
  color: $accent;
}
</style>
