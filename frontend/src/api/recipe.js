import request from './req';


export const apiGetRecipes = () => request('GET', '/recipes');
export const apiCreateRecipe = data => request('POST', '/recipe', data);
export const apiDeleteRecipe = id => request('DELETE', `/recipe/${id}`);
