<template>
    <div class="page-consumer-dashboard">
        <div class="section">
            <div class="container consumer-dash">
                <div class="hero is-info">
                    <div class="hero-body has-text-centered">
                        <p class="title">
                            Welcome to Produce Tracking page
                        </p>
                        <p class="subtitle">
                            Is it realy healthy?
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <hr>
        <div class="section">
            <div class="container search-product">
                <div class="hero is-info">
                    <div class="hero-body has-text-centered field has-addons">
                        <p class="control">
                            <input @keyup.enter="trackProduct()"  v-model="trackId" class="input is-medium" type="text" placeholder="Track product">
                        </p>
                        <p class="button is-info" @click="trackProduct()">
                            <i class="fas fa-search"></i>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="section">
            <div class="container products">
                <p class="has-text-centered title">Products</p>
                <div class="columns is-multiline">
                    <div class="column is-3" v-for="product in products" :key="product.id">
                        <div class="box">
                            <figure class="image mb-4">
                                <img :src="product.image_file" alt="">
                            </figure>
                            <h3 class="is-size-4">
                                {{ product.produce_name }}
                            </h3>
                            <div class="buttons">
                                <RouterLink class="button is-link" :to="{ name: 'farmproducts', params: { product_id: product.id }}">View all {{ product.produce_name }}</RouterLink>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'

export default{
    name: 'ConsumerPageView',
    data () {
        return {
            products: [],
            farmProducts: [],
            trackId: ""
        }
    },
    mounted() {
        this.getProducts();
    },
    methods: {
        async getProducts() {
            await axios
                .get('api/v1/products')
                .then(response => {
                    this.products = response.data;
                })
                .catch(error => {
                    console.log(error);
                })          
        },
        trackProduct() {
            this.$router.push({
                name: 'tracking',
                params: {farmproduct_id: this.trackId}  
            });
        }
    }
}

</script>