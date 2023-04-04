<template>
    <div class="page-farmer-dashboard">
        <div class="section">
            <div class="container farmer-dash">
                <div class="hero">
                    <div class="title">
                        <p class="has-text-centered">Farms</p>
                    </div>
                    <div v-for="farm in farms" :key="farm.id">
                        <div class="box">
                            <h3 class="is-size-4">
                                <RouterLink :to="{name: 'farm', params:{farm_id: farm.id}}">{{ farm.farm_name }}</RouterLink>
                            </h3>
                        </div>
                    </div>
                </div>
                <div class="field-body">
                    <div class="field">
                        <div class="control">
                            <label class="checkbox">
                                <input type="checkbox" v-model="addFarm">
                                    Add farm?
                                </label>
                        </div>
                    </div>
                </div> 
                <div v-if="addFarm" class="box">
                    <div class="field">
                        <label class="label">Farm name</label>
                        <div class="control">
                            <input class="input is-focused" type="text" placeholder="Farm name" v-model="farmName">
                        </div>  
                    </div>
                    <div class="field">
                        <label class="label">Address</label>
                        <div class="control">
                            <input class="input is-focused" type="text" placeholder="Address" v-model="address">
                        </div>  
                    </div>
                    <div class="buttons">
                        <button class="button is-link" @click="addFarms">Submit Farm</button>
                    </div>
                </div>
                <div class="hero">
                    <div class="container">
                        <div class="title">
                            <p class="has-text-centered">Add produce to farm</p>
                        </div>
                        <div class="field-body">
                            <div class="field">
                                <div class="control">
                                    <label class="checkbox">
                                        <input type="checkbox" v-model="addProduce">
                                    Add produce to farm?
                                    </label>
                                </div>
                            </div>
                        </div> 
                        <div v-if="addProduce" class="container">
                            <div class="field">
                                <label class="label">Farm Name</label>
                                <div class="control">
                                    <input class="input is-focused" type="text" placeholder="Farm Name" v-model="selected_farm">
                                </div>
                            </div>
                            <div class="select is-info">
                                <select v-model="selected_product">
                                    <option value="" selected disabled>Choose Product</option>
                                    <option v-for="product in products" :key="product.id">{{ product.produce_name }}</option>
                                </select>
                            </div>
                            <div class="select is-info">
                                <select v-model="selected_farm">
                                    <option value="" selected disabled>Choose Farm</option>
                                    <option v-for="farm in farms" :key="farm.id">{{ farm.farm_name }}</option>
                                </select>
                            </div>
                            <div class="field">
                                <label class="label">Planting Date</label>
                                <div class="control">
                                    <input class="input is-focused" type="date" placeholder="Planting Date" v-model="planting_date">
                                </div>
                            </div>
                            <div class="buttons">
                                <button class="button is-link" @click="addFarmProduce">Submit Product</button>
                            </div>
                        </div>
                        <div class="field-body">
                            <div class="field">
                                <div class="control">
                                    <label class="checkbox">
                                        <input type="checkbox" v-model="addOperation">
                                    Add operation to farm produce?
                                    </label>
                                </div>
                            </div>
                        </div>
                        <div v-if="addOperation" class="container">
                            <div class="field">
                                <label class="label">Operation Name</label>
                                <div class="control">
                                    <input class="input is-focused" type="text" placeholder="Operation Name" v-model="selected_operation">
                                </div>
                            </div>
                            <div class="select is-info">
                                <select v-model="selected_product">
                                    <option value="" selected disabled>Choose Product</option>
                                    <option v-for="product in products" :key="product.id">{{ product.produce_name }}</option>
                                </select>
                            </div>
                            <div class="select is-info">
                                <select v-model="selected_farm" @change="getFarmProducts">
                                    <option value="" selected disabled>Choose Farm</option>
                                    <option v-for="farm in farms" :key="farm.id">{{ farm.farm_name }}</option>
                                </select>
                            </div>
                            <div class="select is-info">
                                <select v-model="selected_farm_produce">
                                    <option value="" selected disabled>Choose Farm Product</option>
                                    <option v-for="farmproduce in farm_products" :key="farmproduce.id">{{ farmproduce.id }} planted on {{ farmproduce.planting_date }}</option>
                                </select>
                            </div>
                            <div class="select is-info">
                                <select v-model="selected_operation">
                                    <option value="" selected disabled>Choose Operation</option>
                                    <option v-for="operation in operations" :key="operation.id">{{ operation.operation_name }}</option>
                                </select>
                            </div>
                            <div class="field">
                                <label class="label">Description</label>
                                <div class="control">
                                    <textarea class="textarea is-link" placeholder="description" v-model="description"></textarea>
                                </div>
                            </div>
                            <div class="field-body">
                                <div class="field">
                                    <div class="control">
                                        <label class="checkbox">
                                            <input type="checkbox" v-model="addInput" @click="getInputs">
                                        Add input to operation?
                                        </label>
                                    </div>
                                </div>                   
                            </div>
                            <div class="field-body">
                                <div class="filed">
                                    <div class="control">
                                        <label class="checkbox">
                                            <input type="checkbox" v-model="createInput">
                                            Create a new input?
                                        </label>
                                    </div>
                                </div>
                            </div>
                            <div v-if="createInput">
                                <div class="buttons">
                                    <RouterLink to="/inputs"><button class="button is-link"></button></RouterLink>>
                                </div>
                            </div>
                            <div  v-if="addInput" class="select is-info">
                                <select v-model="selected_input">
                                    <option value="" selected disabled>Choose input</option>
                                    <option v-for="input in inputs" :key="input.id">{{ input.input_name }} purchased at {{ input.source }}</option>
                                </select>
                            </div>
                            <div class="field">
                                <label class="label">Operation Date</label>
                                <div class="control">
                                    <input class="input is-focused" type="date" placeholder="Operation Name" v-model="operation_date">
                                </div>
                            </div>
                            <div class="buttons">
                                <button class="button is-link" @click="addFarmProduceOperation">Submit Operation</button>
                            </div>
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
    name: 'FarmerPageView',
    data () {
        return {
            farms: [],
            addFarm: false,
            farmName: "",
            address: "",
            farm: {},
            addProduce: false,
            products: [],
            selected_product: "",
            selected_farm: "",
            farm_id: "",
            produce_id: "",
            farmer_id: this.$route.params.farmer_id,
            planting_date: "",
            farm_produce: {},
            addOperation: false,
            selected_operation: "",
            selected_farm_produce: "",
            selected_input: "",
            operations: [],
            operation_date: "",
            farm_products: [],
            operation: {},
            description: "",
            inputs: [],
            addInput: false,
            input_id: "",
            createInput: false
        }
    },
    mounted () {
        this.getFarms();
        this.getProducts();
        this.getOperations();
    },
    methods: {
        async getFarms() {
            await axios
                .get(`api/v1/farmers/${this.farmer_id}/farms`)
                .then(response => {
                    this.farms = response.data;
                })
                .catch(error => {
                    console.log(error);
                })
        },
        async addFarms() {
            const data = {
                farm_name: this.farmName,
                address: this.address
            }
            await axios
                .post(`api/v1/farmers/${this.farmer_id}/farms`, data)
                .then(response => {
                    this.farm = response.data;
                })
                .catch(error => {
                    console.log(error);
                })
        },
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
        async addFarmProduce() {
            for (let i = 0; i < this.farms.length; i++) {
                if (this.farms[i].farm_name === this.selected_farm){
                    this.farm_id = this.farms[i].id;
                }
            }
            for (let i = 0; i < this.products.length; i++) {
                if (this.products[i].produce_name === this.selected_product) {
                    this.produce_id = this.products[i].id;
                }
            }
            const data = {
                planting_date: this.planting_date
            }
            await axios
                .post(`api/v1/farms/${this.farm_id}/products/${this.produce_id}`, data)
                .then(response => {
                    this.farm_produce = response.data;
                    console.log(this.farm_produce);          
                })
                .catch(error => {
                    console.log(error);
                })
        },
        async getOperations() {
            await axios
                .get('api/v1/operations')
                .then(response => {
                    this.operations = response.data;
                })
                .catch(error => {
                    console.log(error);
                })
        },
        async addFarmProduceOperation() {
            for (let i = 0; i < this.farms.length; i++) {
                if (this.farms[i].farm_name === this.selected_farm){
                    this.farm_id = this.farms[i].id;
                }
            }
            for (let i = 0; i < this.products.length; i++) {
                if (this.products[i].produce_name === this.selected_product) {
                    this.produce_id = this.products[i].id;
                }
            }
            for (let i = 0; i < this.operations.length; i++) {
                if(this.operations[i].operation_name === this.selected_operation) {
                    this.operation_id = this.operations[i].id;
                }
            }
            const selected_farm_produce_arr = this.selected_farm_produce.split(" ");
            const farm_produce_id = selected_farm_produce_arr[0];
            const data = {
                operation_date: this.operation_date,
                description: this.description
            }
            if (this.addInput) {
                const selected_input_arr = this.selected_input.split(" ");
                for (let i = 0; i < this.inputs.length; i++){
                    if (this.inputs[i].input_name === selected_input_arr[0]) {
                        this.input_id = this.inputs[i].id;
                    }
                }
                await axios
                    .post(`api/v1/farms/${this.farm_id}/products/${this.produce_id}/${farm_produce_id}/operations/${this.operation_id}/inputs/${this.input_id}`, data)
                    .then(response => {
                        this.operation = response.data;
                        console.log(this.operation);
                    })
                    .catch(error => {
                        console.log(error);
                    })
            } else {
                await axios
                    .post(`api/v1/farms/${this.farm_id}/products/${this.produce_id}/${farm_produce_id}/operations/${this.operation_id}`, data)
                    .then(response => {
                        this.operation = response.data;
                        console.log(this.operation);
                    })
                    .catch(error => {
                        console.log(error);
                    })
            }

        },
        async getFarmProducts() {
            for (let i = 0; i < this.farms.length; i++) {
                if (this.farms[i].farm_name === this.selected_farm){
                    this.farm_id = this.farms[i].id;
                }
            }
            await axios
                .get(`api/v1/farms/${this.farm_id}/products`)
                .then(response => {
                    this.farm_products = response.data;
                })
                .catch(error => {
                    console.log(error);
                })
        },
        async getInputs() {
            await axios
                .get(`api/v1/inputs`)
                .then(response => {
                    this.inputs = response.data;
                })
                .catch(error => {
                    console.log(error);
                })
        }
    }
}
</script>