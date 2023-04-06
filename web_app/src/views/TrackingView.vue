<template>
    <div class="tracking-page">
        <div class="section">
            <div class="container">
                <div class="hero is-info">
                    <p class="has-text-centered title">
                        More info on specific product
                    </p>
                </div>
            </div>
            <hr>
            <div class="columns is-multiline">
                <div class="column is-12 sub-title">
                    <p>Here are the full details</p>
                </div>
                <div class="column is-12" v-for="operation in operations" :key="operation.id">
                    <div class="column is-12 box">
                        <p>Operation {{ operation.operation_name }} carried out on {{ operation.produce_name }}</p>
                        <p>Operation {{ operation.operation_name }} on the {{ operation.operation_date }}</p>
                        <p>Operation description {{ operation.description }}</p>
                        <div class=" column is-6 box" v-for="input in operation.inputs" :key="input.id">
                            <p>Input  {{ input.input_name }}</p>
                            <p>Input Source {{ input.source }}</p>
                            <p>input Pre harvest interval {{ input.pre_harvest_interval }}</p>
                            <p>Input toxicity {{ input.toxicity_level }}</p>
                            <p>Input ingredients {{ input.ingredients }}</p>
                        </div>
                        <div class="container recommendation" v-if="operation.phi_safe && operation.toxic_safe && operation.expiry_safe">
                            <p>Inputs for this operation are safe</p>
                        </div>
                        <div class="container nonrecomm" v-else>
                            <p>Inputs not safe</p>
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
    name: 'TrackingView',
    data () {
        return {
            trackingId: this.$route.params.farmproduct_id,
            operations: [],
            recommended: false
        }
    },
    mounted (){
        this.get_operations_input();
    },
    methods: {
        async get_operations_input() {
            await axios
                .get(`api/v1/farm_products/${this.trackingId}/operations`)
                .then(response => {
                    this.operations = response.data;
                })
                .catch(error => {
                    console.log(error);
                })
        }
    }
}
</script>