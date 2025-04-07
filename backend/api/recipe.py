from fastapi import APIRouter, Depends, HTTPException
from schemas.recipe import recipeSchema, recipeDB
from crud.dependencies import get_recipe_crud
from typing import List
from auth.action import get_current_user
from models.user import UserModels
from crud.recipe import RecipeCRUD  # Typisierung für db

router = APIRouter()

@router.post("/recipe/", response_model=recipeDB)
async def create_recipe_route(
    recipe: recipeSchema,
    current_user: UserModels = Depends(get_current_user),
    db: RecipeCRUD = Depends(get_recipe_crud)
):
    return await db.create_recipe(recipe, current_user=current_user)

@router.put("/recipe/", response_model=recipeDB)
async def update_recipe_route(
    recipe: recipeSchema,
    recipe_id: int,
    current_user: UserModels = Depends(get_current_user),
    db: RecipeCRUD = Depends(get_recipe_crud)
):
    updated = await db.update_recipe(recipe_id, recipe, current_user=current_user)
    if updated is None:
        raise HTTPException(status_code=404, detail="Recipe not found or not owned by user")
    return updated

@router.delete("/recipe/")
async def delete_recipe_route(
    recipe_id: int,
    current_user: UserModels = Depends(get_current_user),
    db: RecipeCRUD = Depends(get_recipe_crud)
):
    result = await db.delete_recipe(recipe_id, current_user=current_user)
    if result is None:
        raise HTTPException(status_code=404, detail="Recipe not found or not owned by user")
    return {"message": "Recipe deleted successfully"}

@router.get("/recipe/", response_model=recipeDB)
async def get_recipe_route(
    recipe_id: int,
    current_user: UserModels = Depends(get_current_user),
    db: RecipeCRUD = Depends(get_recipe_crud)
):
    recipe = await db.get_recipe(recipe_id, current_user=current_user)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found or not owned by user")
    return recipe

@router.get("/recipes/", response_model=List[recipeDB])
async def get_all_recipes_route(
    current_user: UserModels = Depends(get_current_user),
    db: RecipeCRUD = Depends(get_recipe_crud)
):
    recipes = await db.get_all_recipes(current_user=current_user)
    return recipes
