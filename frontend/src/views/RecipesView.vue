<template>
    <div class="mt-5 d-flex justify-content-between">
    <h1 class="mx-5">Recipes</h1>
    <div class="input-group my-3 mx-5" style="width: 18rem;">
        <button class="btn btn-outline-secondary" type="button" id="button-addon1" @click="search">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
            <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/>
            </svg>
        </button>
        <input type="text" class="form-control" placeholder="" aria-label="Example text with button addon" aria-describedby="button-addon1" v-model="searchText">
    </div>
    </div>
    <div class="d-flex m-3 border rounded align-items-center" v-for="recipe in recipeList.value">
        <div class="m-2 ml-3 w-100">
            {{ recipe.title }}
            <p class="text-secondary m-auto">{{ recipe.description_short }}</p>
        </div>
        <div class="m-2 w-25 d-flex justify-content-end">
            {{ recipe.user_id }}
        </div>
        <div class="m-2 mr-4 d-flex justify-content-end w-25">
            {{ new Date(recipe.create_time).toLocaleDateString('de-DE') }}
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useFetchRecipes } from '../store/recipe';
const { recipeList } = useFetchRecipes();

const searchText = ref('');

const search = () => {}

</script>