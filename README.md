## Product Search Application API
- RESTful API for product search application, with **Flask** and **Flask-RESTful** in which JWT authentication is handled by **Flask-JWT**. App is deployed on** Heroku**.
- Additional Library: **SQLAlchemy** as a PostgreSQL tool-kit and ORM.
- Heroku Url: https://stores-flask-restaful.herokuapp.com
- Postman Collection: https://www.getpostman.com/collections/677ba04f25beef3de211

### Requirments
------------
Python 3.5 or higher


### Steps to run the application
------------
1. Use virtual env to install dependencies (You can use `virtualenv` package)
2. Create virtual environment: `virtualenv <env_name>`
3. Activate virtual environment: `source <env_name>/bin/activate` (on Unix)
4. Install dependencies: `pip install requirements.txt`
5. Run the application: `python app.py`

#### Routes:
------------
URL: https://stores-flask-restaful.herokuapp.com
Localhost: http://127.0.0.1:3000
1. Create User -
Route: `POST /signup`
Request Body: `{ "username": string, "password": string}`
1. Authentication -
Route: `POST /login`
Request Body: `{ "username": string, "password": string}`
- All the Routes from now requires authentication:
1. Create New Store -
Route: `POST /store`
Request Body: `{"store_name": string}`
1. Get a Store -
Route: `GET /store/<string:storename>`
1. Delete a Store -
Route: `DELETE store?store_name=string`
1. Get all Stores Detail -
Route: `GET /stores`
1. Create New Item -
Route: `POST /item`
Request Body: `{ "product_name": string, "product_price": float, "store_id": int }`
1. Update an item Price -
Route: `PUT /item/<string:product_name>`
Request Body: `{ "product_price": 20 }`
1. Get an Item Detail -
Route: `GET /item/<string:product_name>`
1. Get all Items -
Route: `/items`
1. Remove Product -
Route: `DELETE item?name=string`

> *Suggestions and Questions are always welcomed, please e-mail me at devashish2910@gmail.com or create an issue*




