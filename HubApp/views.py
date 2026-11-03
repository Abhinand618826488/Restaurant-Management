from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class FoodView(View):
    def get(self, request):
        foods = [
            {
                "id": 101,
                "food_name": "Chicken Biriyani",
                "category": "Main Course",
                "price": 150,
                "description": "Delicious chicken biriyani",
                "availability": True
            },
            {
                "id": 102,
                "food_name": "Veg Fried Rice",
                "category": "Main Course",
                "price": 120,
                "description": "Fresh vegetable fried rice",
                "availability": True
            },
            {
                "id": 103,
                "food_name": "Chocolate Shake",
                "category": "Beverages",
                "price": 90,
                "description": "Cold chocolate milkshake",
                "availability": True
            }
        ]
        return JsonResponse(foods, safe=False)

class FoodDetailView(View):
    def get(self, request, pk):
        foods = [
            {
                "id": 101,
                "food_name": "Chicken Biriyani",
                "category": "Main Course",
                "price": 150,
                "description": "Delicious chicken biriyani",
                "availability": True
            },
            {
                "id": 102,
                "food_name": "Veg Fried Rice",
                "category": "Main Course",
                "price": 120,
                "description": "Fresh vegetable fried rice",
                "availability": True
            },
            {
                "id": 103,
                "food_name": "Chocolate Shake",
                "category": "Beverages",
                "price": 90,
                "description": "Cold chocolate milkshake",
                "availability": True
            }
        ]

        for food in foods:
            if food["id"] == pk:
                return JsonResponse(food)

        return JsonResponse(
            {"message": "Food item not found"},
            status=404
        )
class RestaurantView(View):
    def get(self, request):
        restaurants = [
            {
                "id": 201,
                "restaurant_name": "Food Palace",
                "location": "Kochi",
                "email": "foodpalace@gmail.com",
                "contact": 9876543210,
                "rating": 4.5
            },
            {
                "id": 202,
                "restaurant_name": "Spicy Kitchen",
                "location": "Trivandrum",
                "email": "spicy@gmail.com",
                "contact": 9876543211,
                "rating": 4.2
            }
        ]
        return JsonResponse(restaurants, safe=False)

class CategoryView(View):
    def get(self, request):
        categories = [
            {
                "id": 301,
                "category_name": "Main Course",
                "description": "Rice and main dishes"
            },
            {
                "id": 302,
                "category_name": "Beverages",
                "description": "Juices and drinks"
            },
            {
                "id": 303,
                "category_name": "Desserts",
                "description": "Sweet food items"
            }
        ]
        return JsonResponse(categories, safe=False)