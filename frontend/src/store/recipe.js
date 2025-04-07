import { reactive } from "vue";
import { apiDeleteRecipe, apiGetRecipes, apiCreateRecipe } from "../api/recipe";
import { useLoadingStore } from "./loading";

// data provider pattern : 
// https://www.patterns.dev/vue/data-provider

function useFetchRecipes() {
  const recipeList = reactive([]);

  const fetchRecipes = async () => {
    const loadingStore = useLoadingStore();
    loadingStore.setLoading();

    try {
      const res = await apiGetRecipes();
      recipeList.value = res.data;
    } catch (err) {
      console.log(err);
    } finally {
      // for loading test
      // setTimeout(() => {
      //   loadingStore.clearLoading();
      // }, 1000);
      loadingStore.clearLoading();
    }
  };

  fetchRecipes();

  return { recipeList };
}

async function createRecipe(form){
  const loadingStore = useLoadingStore();
  loadingStore.setLoading();
  console.log(form)

  apiCreateRecipe(form)
}

function removeRecipe(id) {
  const deleteRecipe = async (id) => {
    const loadingStore = useLoadingStore();
    loadingStore.setLoading();

    try {
      await apiDeleteRecipe(id);
    } catch (err) {
      console.log(err);
    } finally {
      loadingStore.clearLoading();
    }
  };

  deleteRecipe(id);
}

export { useFetchRecipes, createRecipe, removeRecipe };