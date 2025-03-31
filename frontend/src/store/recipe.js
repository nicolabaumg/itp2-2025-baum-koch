import { reactive } from "vue";
import { apiGetRecipes } from "../api/recipe";
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

export { useFetchRecipes };