<template>
    <h1 class="mt-5 mx-5">Recipes</h1>
    <div class="m-5">
        <form>
            <form>
            <div class="mb-3">
                <label class="form-label">Title</label>
                <input type="text" class="form-control" v-model="form.title">
            </div>
            <div class="mb-3">
                <label class="form-label">Short description</label>
                <input type="text" class="form-control" v-model="form.shortDescription">
            </div>
            <div class="mb-3">
                <label class="form-label">Long description</label>
                <textarea class="form-control" style="height: 10rem;" v-model="form.longDescription"></textarea>
            </div>
            <button type="submit" class="btn btn-primary" @click="submit">Submit</button>
            <button type="button" class="btn btn-secondary mx-3" @click="$router.push('/myrecipes')">Cancel</button>
            </form>
        </form>
    </div>
</template>

<script>
export default {
    name: 'CreateRecipeView',
    data() {
        return {
            form: {
                title: '',
                shortDescription: '',
                longDescription: ''
            }
        };
    },
    methods: {
        submit() {
            console.log(this.form);
            this.$router.push("/myrecipes");
        }
    },
}
</script>