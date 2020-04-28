from api.routes import app
from flasgger import Swagger
Swagger(app)

if __name__ == '__main__':
    app.run(debug=True)
