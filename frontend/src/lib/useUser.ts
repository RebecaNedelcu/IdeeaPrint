import {reactive} from 'vue';

const state = reactive({
    user: {
        favoriteProducts: [1]
    }
})

export const useUser = () => {
    const isProductFavorite = (productId: number) => {
        return state.user.favoriteProducts.includes(productId)
    }

    return {isProductFavorite, state}
}