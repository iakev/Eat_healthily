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
                        <div class="file">
                            <label class="file-label">
                                <input class="file-input" type="file" @change="checkFile" name="produceImage">
                                <span class="file-cta">
                                    <span class="file-icon"> 
                                        <i class="fas fa-upload"></i>
                                    </span>
                                    <span class="file-label">
                                        Choose a profile pic...
                                    </span>
                                </span> 
                            </label>
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
                        <div class="file">
                            <label class="file-label">
                                <input class="file-input" type="file" @change="checkFarm" name="produceImage">
                                <span class="file-cta">
                                    <span class="file-icon"> 
                                        <i class="fas fa-upload"></i>
                                    </span>
                                    <span class="file-label">
                                        Choose a farm pic...
                                    </span>
                                </span> 
                            </label>
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
            farm: {},
            file: "",
            farmImage: ""
        }
    },
    methods:{
        async consumerSignUp() {
            const headers = { 'Content-Type': 'multipart/form-data' }
            const consumerData =  new FormData();
            consumerData.append('first_name', this.firstName);
            consumerData.append('email', this.email);
            consumerData.append('password', this.password);
            consumerData.append('phone', this.phoneNumber);
            consumerData.append('image_file', this.file);

            await axios
                .post('api/v1/consumers', consumerData, { headers })
                .then(response => {
                    this.consumer = response.data[0];
                    this.$router.push('/login');
                })
                .catch(error => {
                    console.log(error);
                })
        },
        async farmerSignUp() {
            const headers = {
                'Content-Type': 'multipart/form-data'
            }

            const farmerData = new FormData();
            farmerData.append('first_name', this.firstName);
            farmerData.append('last_name', this.lastName);
            farmerData.append('email', this.email);
            farmerData.append('password', this.password,)
            farmerData.append('phone', this.phoneNumber)
            farmerData.append('image_file', this.file);

            const farmData = new FormData();
            farmData.append('farm_name', this.farmName);
            farmData.append('address', this.address);
            farmData.append('image_file', this.farmImage);

            await axios
                .post('api/v1/farmers', farmerData, { headers })
                .then(response => {
                    this.farmer = response.data[0];
                })
                .catch(error => {
                    console.log(error);
                })
            await axios
                .post(`api/v1/farmers/${this.farmer.id}/farms`, farmData, { headers })
                .then(response => {
                    this.farm = response.data[0];
                    this.$router.push('/login');
                })
                .catch(error => {
                    console.log(error);
                })
        },
        checkFile(event) {
            this.file = event.target.files[0];
        },
        checkFarm(event) {
            this.farmImage = event.target.files[0];
        }   
    }
}
</script>