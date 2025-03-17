<template>
    <header>
        <nav class="navbar bg-dark">
            <div class="container-fluid">
                <div class="d-flex">
                    <router-link class="navbar-brand a" to="/">
                        <img src="/logo.png" alt="Bootstrap" width="32" height="32">
                    </router-link>
                    <router-link class="nav-link text-light" to="/">Home</router-link>
                </div>
                <div class="d-flex">
                    <div class="dropdown" v-if="auth.isAuthenticated">
                        <a class="nav-link dropdown-toggle fw-bold text-light" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Profile
                        </a>
                        <ul class="dropdown-menu dropdown-menu-end">
                            <li>
                                <router-link class="nav-link text-dark" to="/profile">View profile</router-link>
                            </li> 
                            <li><hr class="dropdown-divider"></li>
                            <li>
                                <router-link class="nav-link text-dark" to="/logout">Logout</router-link>
                            </li>
                        </ul>
                    </div>
                    <div class="d-flex" v-else>
                        <router-link class="nav-link text-light" to="/register">Register</router-link>
                        <router-link class="nav-link text-light" to="/login">Login</router-link>
                    </div>
                </div>
            </div>
        </nav>
    </header>
</template>
  
<script setup>
import { useAuthStore } from '../store/auth';
import { useProfile } from '../store/me';
const auth = useAuthStore();

const { 
    me,
    reloadData,
    updatePassword,
    updateBirthday,
    changeAccessToken,
} = useProfile();

</script>
  
<style scoped>
a {
    cursor: pointer;
}

.a {
    color: black !important;
}
</style>
  