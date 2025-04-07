<template>
    <div class="mt-5 d-flex justify-content-between">
    <h1 class="mx-5">My Recipes</h1>
    <div class="input-group my-3 mx-5" style="width: 18rem;">
        <router-link class="btn btn-success" type="button" to="/create">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-circle" viewBox="0 0 16 16">
                <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4"/>
            </svg>
            Create new recipe
        </router-link>
    </div>
    </div>
    <div class="d-flex m-3 border rounded align-items-center" v-for="recipe in recipeList.value.filter(recipe => recipe.user_id === me.username)">
        <div class="m-2 ml-3 w-100">
            {{ recipe.title }}
            <p class="text-secondary m-auto">{{ recipe.description_short }}</p>
        </div>
        <div class="m-2 mr-4 d-flex justify-content-end w-50">
            {{ new Date(recipe.create_time).toLocaleDateString('de-DE') }}
        </div>
        <button class="btn btn-danger mr-3" @click="handleRemoveRecipe(recipe.id)">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
            <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"/>
            <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"/>
            </svg>
        </button>
    </div>
</template>

<script setup>
import { useFetchRecipes, removeRecipe } from '../store/recipe';
import { useProfile } from '../store/me';
import router from '../router';
const {recipeList} = useFetchRecipes();

const { 
    me,
    reloadData,
    updatePassword,
    updateBirthday,
    changeAccessToken,
} = useProfile();

const handleRemoveRecipe = async (recipeId) => {
    await removeRecipe(recipeId);
    recipeList.value = recipeList.value.filter(recipe => recipe.id !== recipeId);
};
</script>