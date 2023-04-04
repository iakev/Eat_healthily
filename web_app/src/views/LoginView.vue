<template>
    <div class="login-view">
        <div class="section">
            <div class="container">
                <div class="section">
                    <div class="container user-login">
                        <div class="field">
                            <label class="label">Email</label>
                            <div class="control">
                                <input class="input is-focused" type="text" placeholder="Email" v-model="email">
                            </div>
                        </div>
                        <div class="filed">
                            <label class="label">Password</label>
                            <div class="control">
                                <input class="input is-focused" type="password" placeholder="Password" v-model="password">
                            </div>
                        </div>
                    </div>
                </div>
                <div class="buttons">
                    <button class="button is-link" @click="userLogin">Login</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { useUserStore } from '../stores/users';

export default{
    setup() {
        const userStore = useUserStore();
        return { userStore };
    },
    name: "LoginView",
    data () {
        return {
            email: "",
            password: "",
            authenticated: false,
            user: {}
        }
    },
    methods: {
        async userLogin() {
            const data = {
                email: this.email,
                password: this.password
            }
            if (this.email === "" || this.password === "") {
                alert('The email and password must be present!')
            }
            else {
                await axios
                    .post('api/v1/users/login', data)
                    .then(response => {
                        this.user = response.data;
                        this.authenticated = this.user.authenticated;
                        if (this.authenticated) {
                            this.userStore.user = this.user;
                        if (this.user.type === 'farmer') {
                            this.$router.push({
                                name: 'farmer',
                                params: {farmer_id: this.user.id}
                            });
                        } else {
                            this.$router.push('/consumerdash');
                        }
                    } else {
                        alert("incorrect email or password");
                    }
                    })
                    .catch(error => {
                        console.log(error);
                    })
                }
        }
    }
}
</script>