<template>
    <h1 class="mt-5 mx-5">Recipes</h1>
    <div class="m-5">
        <form @submit.prevent="submit">
            <div class="mb-3">
                <label class="form-label">Title</label>
                <input type="text" class="form-control" v-model="form.title">
            </div>
            <div class="mb-3">
                <label class="form-label">Short description</label>
                <input type="text" class="form-control" v-model="form.description_short">
            </div>
            <div class="mb-3">
                <label class="form-label">Long description</label>
                <textarea class="form-control" style="height: 10rem;" v-model="form.description_long"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
            <button type="button" class="btn btn-secondary mx-3" @click="$router.push('/myrecipes')">Cancel</button>
        </form>
    </div>
</template>

<script>
import { useProfile } from '../store/me';
import { createRecipe } from '../store/recipe';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const { 
      me,
      reloadData,
      updatePassword,
      updateBirthday,
      changeAccessToken,
    } = useProfile();

    const router = useRouter();

    const form = ref({
      title: '',
      description_short: '',
      description_long: '',
      user_id: '',
      create_time: null
    });

    const submit = async () => {
      createRecipe(form.value)
      router.push('/myrecipes')
    };

    return {
      form,
      submit,
    };
  },
};
</script>