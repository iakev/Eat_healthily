<template>
    <div class="create-operation">
        <div class="section create-operation">
            <div class="container">
                <div class="hero is-info">
                    <div class="hero-body has-text-centered">
                        <p class="title">
                            Create Operation
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <hr>
        <div class="section">
            <div class="container">
                <div class="field">
                    <label class="label">Operation name</label>
                    <div class="control">
                        <input class="input is-focused" type="text" placeholder="Produce Name" v-model="operationName">
                    </div>
                </div>
                <br>
                <div class="buttons">
                    <button class="button is-link" @click="onSubmit">Add Operation</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'OperationView',
    data () {
        return {
            operationName: "",
            operation: {}
        }
    },
    methods: {
        reloadPage() {
            window.location.reload();
        },
        async onSubmit() {
            const data = {
                operation_name: this.operationName
            }

            await axios
                .post('api/v1/operations', data)
                .then(response => {
                    this.operation = response.data;
                    alert('Operation added succesfully');
                    this.reloadPage();
                })
                .catch(error => {
                    console.log(error);
                })
        }
    }
}
</script>