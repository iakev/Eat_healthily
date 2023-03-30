import { defineStore } from 'pinia';
import axios from 'axios';

export const useProductStore = defineStore("product", {
    state: () => ({
        products: [],
        product: null,
    }),

    actions: {
        async getProducts() {
            await axios
                .get('api/v1/products')
                .then(response => {
                    this.products = response.data;
                })
        }
    },
});