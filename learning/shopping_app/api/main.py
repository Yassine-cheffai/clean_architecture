from flask import Flask
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request

app = Flask(__name__)
db = SQLAlchemy()
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
migrate = Migrate(app, db)

food_model = api.model(
    "food",
    {
        "category": fields.String,
        "name": fields.String,
        "price": fields.Integer,
        "stacked": fields.Boolean,
    },
)


class Food(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    category: str = db.Column(db.String)
    name: str = db.Column(db.String)
    price: int = db.Column(db.Integer)
    stacked: bool = db.Column(db.Boolean)

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"{self.name}"


@api.route("/foods")
class FoodApi(Resource):
    @api.marshal_list_with(food_model)
    def get(self):
        foods = [
            {
                "id": food.id,
                "category": food.category,
                "name": food.name,
                "stacked": food.stacked,
                "price": food.price,
            }
            for food in Food.query.all()
        ]
        return foods

    @api.expect(food_model)
    @api.marshal_with(food_model)
    def post(self):
        data = request.json
        food = Food(
            category=data["category"],
            name=data["name"],
            price=data["price"],
            stacked=data["stacked"],
        )
        db.session.add(food)
        db.session.commit()

        return {
            "category": food.category,
            "name": food.name,
            "stacked": food.stacked,
            "price": food.price,
        }, 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
