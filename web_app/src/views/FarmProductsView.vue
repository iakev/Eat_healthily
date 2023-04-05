<template> 
    <div class="page-farm-products">
        <div class="section">
            <div class="container farm-products">
                <div class="hero is-info">
                    <p class="has-text-centered title">
                        Here are the trackable products
                    </p>
                </div>
            </div>
        </div>
        <hr>
        <div class="columns is-multiline">
            <div class="column is-12 title">
                <p class="has-text-centered">Farm Products</p>
            </div>
            <div class="column is-6" v-for="farmProduce in farmProducts" :key="farmProduce.id">
                <div class="column is-6 box">
                    <figure class="image mb-4">
                        <img :src="farmProduce.image_file" alt="">
                    </figure>
                    <p> Produce name {{ farmProduce.produce_name }}</p>
                    <p>Farm name {{ farmProduce.farm_name }} at {{ farmProduce.address }}</p>
                    <p>Planted on {{ farmProduce.planting_date }} and harvested on {{ farmProduce.harvest_date }}</p>
                    <p>Tracking id <RouterLink :to="{name: 'tracking', params: {farmproduct_id: farmProduce.id}}">{{ farmProduce.id }}</RouterLink></p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'FarmProductsView',
    data () {
        return {
            farmProducts: []
        }
    },
    mounted () {
        this.getFarmProducts();
    },
    methods: {
        async getFarmProducts() {
            const product_id = this.$route.params.product_id;
            await axios
                .get(`api/v1/products/${product_id}`)
                .then(response => {
                    this.farmProducts = response.data;
                })
                .catch(error => {
                    console.log(error);
                })
               
        }
    }
}
</script>