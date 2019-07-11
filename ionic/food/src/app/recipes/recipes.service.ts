import { Injectable } from '@angular/core';
import { Recipe } from './recipe.model';

@Injectable({
  providedIn: 'root'
})
export class RecipesService {

  private recipes: Recipe[] = [
    {
      id: 'r1',
      title: 'Apple Pie',
      imageUrl: 'https://bit.ly/2XFXUfC',
      ingredients: ['apples', 'sugar', 'salt', 'nutmeg']
    },
    {
      id: 'r2',
      title: 'Chocolate Chip Cookies',
      imageUrl: 'https://bit.ly/2xHuAWg',
      ingredients: ['flour', 'chocolate', 'brown sugar', 'vanilla extract']
    }
  ];


  constructor() { }

  getAllRecipes() {
    return [...this.recipes];
  }

  getRecipe(recipeId: string) {
    return {...this.recipes.find(recipe => recipe.id === recipeId)};
  }

  deleteRecipe(recipeId: string) {
    this.recipes = this.recipes.filter(recipe => recipe.id !== recipeId);
  }
}
