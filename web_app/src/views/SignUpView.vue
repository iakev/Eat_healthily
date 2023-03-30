<template>
    <div class="page-signup">
        <div class="section">
            <div class="container">
                <div class="section">
                    <div class="container consumer-signup">
                        <div class="field">
                            <label class="label">First Name</label>
                            <div class="control">
                                <input class="input is-focused" type="text" placeholder="First Name" v-model="firstName">
                            </div>  
                        </div>
                        <div class="field">
                            <label class="label">Last Name</label>
                            <div class="control">
                                <input class="input is-focused" type="text" placeholder="Last Name" v-model="lastName">
                            </div>  
                        </div>
                        <div class="field">
                            <label class="label">Email</label>
                            <div class="control">
                                <input class="input is-focused" type="text" placeholder="Email" v-model="email">
                            </div>  
                        </div>
                        <div class="field">
                            <label class="label">Phone Number</label>
                            <div class="control">
                                <input class="input is-focused" type="text" placeholder="Phone Number" v-model="phoneNumber">
                            </div>  
                        </div>
                        <div class="field">
                            <label class="label">Enter Password</label>
                            <div class="control">
                                <input class="input is-focused" type="password" placeholder="Enter Password" v-model="password">
                            </div>  
                        </div>
                        <div class="field-body">
                            <div class="field">
                                <div class="control">
                                    <label class="checkbox">
                                        <input type="checkbox" v-model="isFarmer">
                                        Is Farmer?
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div v-if="isFarmer" class="section">
                    <div class="container farmer-signup">
                        <div class="field">
                            <label class="label">Farm Name</label>
                                <div class="control">
                                    <input class="input is-focused" type="text" placeholder="Farm Name" v-model="farmName">
                                </div>  
                        </div>
                        <div class="field">
                            <label class="label">Address</label>
                            <div class="control">
                                <input class="input is-focused" type="text" placeholder="Address" v-model="address">
                            </div>  
                        </div>
                    </div>
                </div>
                <div class="buttons">
                    <button v-if="isFarmer" class="button is-link" @click="farmerSignUp">Farmer Sign Up</button>
                    <button v-else class="button is-link" @click="consumerSignUp">Consumer Sign Up</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import  axios from 'axios';

export default{
    name: 'SignUpView',
    data() {
        return {
            firstName: "",
            lastName: "",
            email: "",
            phoneNumber:"",
            password: "",
            isFarmer: false,
            farmName: "",
            address: "",
            consumer: {},
            farmer: {},
            farm: {}
        }
    },
    methods:{
        async consumerSignUp() {
            const data = {
                first_name: this.firstName,
                last_name: this.lastName,
                email: this.email,
                password: this.password,
                phone: this.phoneNumber
            }
            await axios
                .post('api/v1/consumers', data)
                .then(response => {
                    this.consumer = response.data[0];
                    this.$router.push('/login');
                })
                .catch(error => {
                    console.log(error);
                })
        },
        async farmerSignUp() {
            const farmerData = {
                first_name: this.firstName,
                last_name: this.lastName,
                email: this.email,
                password: this.password,
                phone: this.phoneNumber
            }
            const farmData = {
                farm_name: this.farmName,
                address: this.address
            }
            await axios
                .post('api/v1/farmers', farmerData)
                .then(response => {
                    this.farmer = response.data[0];
                })
                .catch(error => {
                    console.log(error);
                })
            await axios
                .post(`api/v1/farmers/${this.farmer.id}/farms`, farmData)
                .then(response => {
                    this.farm = response.data[0];
                    this.$router.push('/login');
                })
                .catch(error => {
                    console.log(error);
                })
        }   
    }
}
</script>