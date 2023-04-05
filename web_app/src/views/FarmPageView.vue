<template>
    <div class="page-farm">
        <div class="section">
            <div class="container farm">
                <div class="hero is-info">
                    <div class="hero-body has-text-centered">
                        <p class="title">
                            Welcome, here are the products
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <hr>
        <div class="section">
            <div class="container farm-products">
                <p class="has-text-centered title">Farm products</p>
                <div class="columns multiline">
                    <div class="column is-3" v-for="farmProduce in farmProducts" :key="farmProduce.id">
                        <div class="box">
                            <figure class="image mb-4">
                                <img :src="farmProduce.image_file" alt="">
                            </figure>
                           <p>{{ farmProduce.produce_name }} planted on {{ farmProduce.planting_date }}</p> 
                           <p>Harvested on {{ farmProduce.harvest_date }}</p>
                           <p>Tracking id <RouterLink :to="{name: 'tracking', params: {farmproduct_id: farmProduce.id}}">{{ farmProduce.id }}</RouterLink></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default{
    name: 'FarmPageView',
    data () {
        return {
            farm_id: this.$route.params.farm_id,
            farmProducts: []
        }
    },
    mounted(){
        this.getFarmProducts();
    },
    methods: {
        async getFarmProducts() {
            await axios
                .get(`api/v1/farms/${this.farm_id}/products`)
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