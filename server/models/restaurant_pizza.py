from server import db

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    
    # Foreign keys
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    
    def __repr__(self):
        return f'<RestaurantPizza ${self.price}>'
    
    # Validation method
    def validate_price(self):
        if not 1 <= self.price <= 30:
            raise ValueError("Price must be between 1 and 30")