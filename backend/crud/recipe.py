from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.recipe import RecipeModels
from schemas.recipe import recipeSchema, recipeDB
from typing import List
from models.user import UserModels

class RecipeCRUD:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_recipe(self, recipe: recipeSchema, current_user: UserModels):
        db_recipe = RecipeModels(
            title=recipe.title,
            description_short=recipe.description_short,
            description_long=recipe.description_long,
            user_id=current_user.username
        )
        self.db_session.add(db_recipe)
        await self.db_session.commit()
        await self.db_session.refresh(db_recipe)
        return db_recipe

    async def update_recipe(self, recipe_id: int, recipe: recipeSchema, current_user: UserModels):
        stmt = select(RecipeModels).where(
            RecipeModels.id == recipe_id,
            RecipeModels.user_id == current_user.username
        )
        result = await self.db_session.execute(stmt)
        found_recipe = result.scalars().first()

        if found_recipe is None:
            return None

        found_recipe.title = recipe.title
        found_recipe.description_short = recipe.description_short
        found_recipe.description_long = recipe.description_long

        await self.db_session.commit()
        await self.db_session.refresh(found_recipe)
        return found_recipe

    async def delete_recipe(self, recipe_id: int, current_user: UserModels):
        stmt = select(RecipeModels).where(
            RecipeModels.id == recipe_id,
            RecipeModels.user_id == current_user.username
        )
        result = await self.db_session.execute(stmt)
        found_recipe = result.scalars().first()

        if found_recipe is None:
            return None

        await self.db_session.delete(found_recipe)
        await self.db_session.commit()
        return found_recipe

    async def get_recipe(self, recipe_id: int, current_user: UserModels):
        stmt = select(RecipeModels).where(
            RecipeModels.id == recipe_id,
            RecipeModels.user_id == current_user.username
        )
        result = await self.db_session.execute(stmt)
        return result.scalars().first()

    async def get_all_recipes(self, current_user: UserModels) -> List[recipeDB]:
        stmt = select(RecipeModels)
        result = await self.db_session.execute(stmt)
        return result.scalars().all()
