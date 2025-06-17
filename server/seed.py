from .app import app
from . import db
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza

def seed_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create restaurants
        restaurants = [
            Restaurant(name="Pizza Palace", address="123 Main St"),
            Restaurant(name="Italian Bistro", address="456 Oak Ave"),
            Restaurant(name="Mama Mia's", address="789 Pine Rd")
        ]
        db.session.add_all(restaurants)
        db.session.commit()

        # Create pizzas
        pizzas = [
            Pizza(name="Margherita", ingredients="Tomato sauce, mozzarella, basil"),
            Pizza(name="Pepperoni", ingredients="Tomato sauce, mozzarella, pepperoni"),
            Pizza(name="Vegetarian", ingredients="Tomato sauce, mozzarella, bell peppers, mushrooms")
        ]
        db.session.add_all(pizzas)
        db.session.commit()

        # Create restaurant_pizzas
        restaurant_pizzas = [
            RestaurantPizza(price=10, restaurant_id=1, pizza_id=1),
            RestaurantPizza(price=12, restaurant_id=1, pizza_id=2),
            RestaurantPizza(price=15, restaurant_id=2, pizza_id=1),
            RestaurantPizza(price=14, restaurant_id=2, pizza_id=3),
            RestaurantPizza(price=11, restaurant_id=3, pizza_id=2),
            RestaurantPizza(price=13, restaurant_id=3, pizza_id=3)
        ]
        db.session.add_all(restaurant_pizzas)
        db.session.commit()

        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()