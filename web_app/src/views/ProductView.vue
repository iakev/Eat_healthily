<template>
    <div class="create-product">
        <div class="section create-product">
            <div class="container">
                <div class="hero  is-info">
                    <div class="hero-body has-text-centered">
                        <p class="title">
                            Create product
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <hr>
        <div class="section">
            <div class="container">
                <div class="field">
                    <label class="label">Produce name</label>
                    <div class="control">
                        <input class="input is-focused" type="text" placeholder="Produce Name" v-model="productName">
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
                                Choose a file...
                            </span>
                        </span> 
                    </label>
                </div>
                <hr>
                <div class="buttons">
                    <button class="button is-link" @click="onSubmit">Add produce</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'ProductView',
    data () {
        return {
            productName: "",
            file: "",
            product: {}
        }
    },
    methods: {
        reloadPage() {
            window.location.reload();
        },
        checkFile(event) {
            this.file = event.target.files[0];
        },
        onSubmit() {
            const payload = new FormData();
            payload.append('produce_name', this.productName);
            payload.append('image_file', this.file);

            this.createProduct(payload);
        },
        async createProduct(payload) {
            const headers = {
                'Content-Type': 'multipart/form-data'
            }
            await axios
                .post('api/v1/products', payload, { headers })
                .then(response => {
                    this.product = response.data;
                    alert('Succesfuly added');
                    this.reloadPage();
                })
                .catch(error => {
                    console.log(error);
                })
        }
    }
}
</script>