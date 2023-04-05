<template>
    <div class="container page-input">
        <div class="section">
            <div class="hero is-info">
                <div class="hero-body has-text-centered">
                    <p class="title">Add input</p>
                </div>
            </div>
        </div>
        <div class="section">
            <div class="container">
                <div class="field">
                    <label class="label">Input name</label>
                    <div class="control">
                        <input class="input is-focused" type="text" placeholder="Input Name" v-model="inputName">
                    </div>
                </div>
                <div class="field">
                    <label class="label">Manufacturing Date</label>
                    <div class="control">
                        <input class="input is-focused" type="date" placeholder="Manufacturing date" v-model="mnfgDate">
                    </div>
                </div>
                <div class="field">
                    <label class="label">Expiry Date</label>
                    <div class="control">
                        <input class="input is-focused" type="date" placeholder="Expiry Date" v-model="expDate">
                    </div>
                </div>
                <div class="field">
                    <label class="label">Cautions</label>
                    <div class="control">
                        <input class="input is-focused" type="text" placeholder="Cautions" v-model="caution">
                    </div>
                </div>
                <div class="field">
                    <label class="label">Input source</label>
                    <div class="control">
                        <input class="input is-focused" type="text" placeholder="Input Source" v-model="inputSource">
                    </div>
                </div>
                <div class="field">
                    <label class="label">Pre Harvest Interval in days</label>
                    <div class="control">
                        <input class="input is-focused" type="text" placeholder="Pre Harvest Interval" v-model="phi">
                    </div>
                </div>
                <!-- <div class="field">
                    <label class="label">Toxicity Level</label>
                    <div class="control">
                        <input class="input is-focused" type="text" placeholder="Toxicity Level" v-model="toxiciyLevel">
                    </div>
                </div> -->
                <div class="select is-info">
                    <select v-model="toxiciyLevel">
                        <option value="" selected disabled>Choose Toxicity level</option>
                        <option value="1">Highly Toxic</option>
                        <option value="2">Toxic</option>
                        <option value="3">Moderately Toxic</option>
                        <option value="4">Slightly Toxic</option>
                        <option value="5">Virtually non-toxic</option>
                    </select>
                </div>
                <div class="field">
                    <label class="label">Ingredient</label>
                    <div class="control">
                        <input class="input is-focused" type="text" placeholder="Ingredient" v-model="ingredient">
                    </div>
                </div>
                <div class="file">
                    <label class="file-label">
                        <input class="file-input" type="file" @change="checkImage" name="image_file" >
                        <span class="file-cta">
                            <span class="file-icon"> 
                                <i class="fas fa-upload"></i>
                            </span>
                            <span class="file-label">
                                Choose a input Image...
                            </span>
                        </span>
                    </label>
                </div>
                <hr>
                <div class="file">
                    <label class="file-label">
                        <input class="file-input" type="file"  @change="checkLabel" name="label_file">
                        <span class="file-cta">
                            <span class="file-icon"> 
                                <i class="fas fa-upload"></i>
                            </span>
                            <span class="file-label">
                                Choose a input label...
                            </span>
                        </span>
                    </label>
                </div>
                <hr>
                <div class="file">
                    <label class="file-label">
                        <input class="file-input" type="file"  @change="checkManual" name="user_manual_file">
                        <span class="file-cta">
                            <span class="file-icon"> 
                                <i class="fas fa-upload"></i>
                            </span>
                            <span class="file-label">
                                Choose input manual...
                            </span>
                        </span>
                    </label>
                </div>
                <hr>
                <div class="buttons">
                    <button class="button is-link" @click="onSubmit">Add input</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'InputView',
    data () {
        return {
            inputName: "",
            mnfgDate: "",
            expDate: "",
            caution: "",
            inputSource: "",
            phi: "",
            toxiciyLevel: "",
            ingredient: "",
            input: {},
            image: "",
            label: "",
            manual: ""
        }
    },
    methods: {
        reloadPage() {
            window.location.reload();
        },
        checkImage(event) {
            this.image = event.target.files[0];
        },
        checkLabel(event) {
            this.label = event.target.files[0];
        },
        checkManual(event) {
            this.manual = event.target.files[0];
        },
        onSubmit() {
            const payload = new FormData();
            payload.append('input_name', this.inputName);
            payload.append('manufactring_date', this.mnfgDate);
            payload.append('expiry_date', this.expDate);
            payload.append('source', this.inputSource);
            payload.append('cautions', this.caution);
            payload.append('pre_harvest_interval', this.phi);
            payload.append('toxicity_level', this.toxiciyLevel);
            payload.append('ingredient', this.ingredient);
            payload.append('image_file', this.image);
            payload.append('label_file', this.label);
            payload.append('user_manual_file', this.manual);

            this.createInput(payload);
        },
        async createInput(payload) {
            const headers = {
                'Content-Type': 'multipart/form-data'
            }
            await axios
                .post('api/v1/inputs', payload, { headers })
                .then(response => {
                    this.input = response.data;
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