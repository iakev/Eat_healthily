<template>
    <div class="container page-input">
        <div class="section">
            <div class="hero">
                <div class="hero-body">
                    <p class="text-is-centered">Add input</p>
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
                        <input class="input is-focused" type="text" placeholder="Manufacturing date" v-model="mnfgDate">
                    </div>
                </div>
                <div class="field">
                    <label class="label">Expiry Date</label>
                    <div class="control">
                        <input class="input is-focused" type="text" placeholder="Expiry Date" v-model="expDate">
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
                <div class="field">
                    <label class="label">Toxicity Level</label>
                    <div class="control">
                        <input class="input is-focused" type="text" placeholder="Toxicity Level" v-model="toxiciyLevel">
                    </div>
                </div>
                <div class="field">
                    <label class="label">Ingredient</label>
                    <div class="control">
                        <input class="input is-focused" type="text" placeholder="Ingredient" v-model="ingredient">
                    </div>
                </div>
                <div class="file">
                    <label class="file-label">
                        <input class="file-input" type="file" name="image_file">
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
                <div class="file">
                    <label class="file-label">
                        <input class="file-input" type="file" name="label_file">
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
                <div class="file">
                    <label class="file-label">
                        <input class="file-input" type="file" name="user_manual_file">
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
            ingredient: ""
        }
    }
}
</script>