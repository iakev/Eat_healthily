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
                    <label class="label">Input name</label>
                    <div class="control">
                        <input class="input is-focused" type="text" placeholder="Input Name" v-model="selected_input">
                    </div>
                </div>
                <div class="field">
                    <label class="label">Input source</label>
                    <div class="control">
                        <input class="input is-focused" type="text" placeholder="Input Source" v-model="selected_source">
                    </div>
                </div>
                <div class="file">
                    <label class="file-label">
                        <input class="file-input" type="file" name="inputImage">
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
    name: 'ProductView',
    data () {
        return {
            selected_input: "",
            selected_source: "",
            selected_image: ""
        }
    }
}
</script>