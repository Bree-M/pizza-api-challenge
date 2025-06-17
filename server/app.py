from . import create_app, db
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza
from .controllers.restaurant_controller import restaurant_bp
from .controllers.pizza_controller import pizza_bp
from .controllers.restaurant_pizza_controller import restaurant_pizza_bp

app = create_app()

# Register blueprints
app.register_blueprint(restaurant_bp, url_prefix='/')
app.register_blueprint(pizza_bp, url_prefix='/')
app.register_blueprint(restaurant_pizza_bp, url_prefix='/')

@app.route('/')
def home():
    return "Welcome to the Pizza Restaurant API!"

if __name__ == '__main__':
    app.run(port=5555, debug=True)