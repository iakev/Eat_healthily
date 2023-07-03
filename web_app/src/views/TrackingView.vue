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
                <div class="column is-12">
                    <div class="column is-12 box">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Operation Name</th>
                                    <th></th>
                                    <th>Operation Date</th>
                                    <th></th>
                                    <th>Description</th>
                                    <th>Inputs</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="operation in operations" :key="operation.id">
                                    <td>{{ operation.operation_name }}</td>
                                    <td>{{  }}</td>
                                    <td>{{ operation.operation_date }}</td>
                                    <td>{{  }}</td>
                                    <td>{{ operation.description }}</td>
                                    <td v-if="operation.inputs.length !== 0">
                                        <div class="column is-12" v-for="input in operation.inputs">
                                            <p>input Name {{ input.input_name }}</p>
                                            <p>source {{ input.source }}</p>
                                            <p> Pre-harvest interval {{ input.pre_harvest_interval }} days</p>
                                            <p>{{ input.toxicity_level }}</p>
                                            <p>{{ input.ingredients }}</p>
                                            <div class="container recommendation" v-if="operation.phi_safe && operation.toxic_safe && operation.expiry_safe">
                                                <p><b>Inputs for this operation are safe</b>b></p>
                                            </div>
                                            <div class="container nonrecomm" v-else>
                                                <p><b>Inputs not safe</b></p>
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <!-- <div class="column is-6 box" v-for="operation in operations" :key="operation.id">
                            <table>
                                <thead>
                                    <tr>
                                        <th>Name</th>
                                        <th>Source</th>
                                        <th>Pre-harverst Interval</th>
                                        <th>Toxicity</th>
                                        <th>Ingredients</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="input in operation.inputs" :key="input.id">
                                        <td>{{ input.name }}</td>
                                        <td>{{ input.source }}</td>
                                        <td>{{ input.pre_harvest_interval }}</td>
                                        <td>{{ input.toxicity_level }}</td>
                                        <td>{{ input.ingredients }}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div> -->
                        <!-- <p>Operation {{ operation.operation_name }} carried out on {{ operation.produce_name }}</p>
                        <p>Operation {{ operation.operation_name }} on the {{ operation.operation_date }}</p>
                        <p>Operation description {{ operation.description }}</p>
                        <div class=" column is-6 box" v-for="input in operation.inputs" :key="input.id">
                            <p>Input  {{ input.input_name }}</p>
                            <p>Input Source {{ input.source }}</p>
                            <p>input Pre harvest interval {{ input.pre_harvest_interval }}</p>
                            <p>Input toxicity {{ input.toxicity_level }}</p>
                            <p>Input ingredients {{ input.ingredients }}</p>
                        </div> -->
                        <!-- <div class="container recommendation" v-if="operation.phi_safe && operation.toxic_safe && operation.expiry_safe">
                            <p>Inputs for this operation are safe</p>
                        </div>
                        <div class="container nonrecomm" v-else>
                            <p>Inputs not safe</p>
                        </div> -->
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
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
                    response.data.sort((a, b) => {
                        const A = new Date(a.operation_date);
                        const B = new Date(b.operation_date);
                        return A - B;
                    })
                    this.operations = response.data;
                })
                .catch(error => {
                    console.log(error);
                })
        }
    }
}
</script>