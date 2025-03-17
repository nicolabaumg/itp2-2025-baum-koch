from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.recipe import RecipeModels
from models.steps import StepsModels
from schemas.recipe import recipeSchema, recipeDB
from typing import List

class RecipeCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def create_recipe(self, recipe: recipeSchema):
        db_recipe = RecipeModels(
            title = recipe.title,
            description = recipe.description
        )
        self.db_session.add(db_recipe)
        await self.db_session.commit()
        await self.db_session.refresh(db_recipe)


        for step in recipe.steps:
            new_step = StepsModels(recipe_id = db_recipe.id, text = step.text)
            self.db_session.add(new_step)
        await self.db_session.commit()
    
        return db_recipe
    
    async def update_recipe(self, recipe_id, recipe: recipeSchema):
        stmt = select(RecipeModels).where(RecipeModels.id == recipe_id)
        result = await self.db_session.execute(stmt)
        found_recipe = result.scalars().first()

        if found_recipe == None:
            return None
        
        new_recipe = RecipeModels(
            title = recipe.title,
            description = recipe.description
        )
        self.db_session.add(new_recipe)
        await self.db_session.commit()

        for step in recipe.steps:
            new_step = StepsModels(recipe_id = new_recipe.id, text = step.text)
            self.db_session.add(new_step)
        await self.db_session.commit()

        return new_recipe
    
    async def delete_recipe(self, recipe_id):
        stmt = select(RecipeModels).where(RecipeModels.id == recipe_id)
        result = await self.db_session.execute(stmt)
        found_recipe = result.scalars().first()

        if found_recipe == None:
            return None
        
        await self.db_session.delete(found_recipe)
        await self.db_session.commit()

    async def get_recipe(self, recipe_id, recipe: recipeSchema):
        stmt = select(RecipeModels).where(RecipeModels.id == recipe_id)
        result = await self.db_session.execute(stmt)
        found_recipe = result.scalars().first()

        return found_recipe
    
    async def get_all_recipes(self) -> List[recipeDB]:
        stmt = select(RecipeModels)
        result = await self.db_session.execute(stmt)
        all_recipes = result.scalars().all()
        return all_recipes