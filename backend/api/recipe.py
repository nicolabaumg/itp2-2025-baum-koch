from fastapi import APIRouter, Depends, HTTPException
from schemas.recipe import recipeSchema, recipeDB
from crud.dependencies import get_recipe_crud
from typing import List

router = APIRouter()

@router.post("/recipe/", response_model=recipeDB)
async def create_recipe_route(recipe: recipeSchema, db: recipeDB = Depends(get_recipe_crud)):
    return await db.create_recipe(recipe)

@router.put("/recipe/", response_model=recipeDB)
async def update_recipe_route(recipe, recipe_id: int, db: recipeDB = Depends(get_recipe_crud)):
    recipe = await db.update_recipe(recipe_id, recipe)
    if recipe is None: 
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.delete("/recipe/", response_model=recipeDB)
async def delete_recipe_route(recipe_id: int, db: recipeDB = Depends(get_recipe_crud)):
    success = await db.delete_recipe(recipe_id)
    if not success:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"message": "Recipe deleted successfully"}

@router.get("/recipe/", response_model=recipeDB)
async def get_recipe_route(recipe_id: int, db: recipeDB = Depends(get_recipe_crud)):
    recipe = await db.get_recipe(recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.get("/recipe/", response_model=List[recipeDB])
async def get_all_recipes_route(db: recipeDB = Depends(get_recipe_crud)):
    recipes = await db.get_all_recipes()
    if not recipes:
        raise HTTPException(status_code=404, detail="Recipes not found")
    return recipes
