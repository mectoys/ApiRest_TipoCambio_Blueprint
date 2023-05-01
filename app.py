from flask import Flask, render_template
from scr.config import config
from scr.routes import Exchange

app = Flask(__name__)


def pagina_no_encontrada(error):
    # return "<h1>La página que intentas buscar no existe...</h1>"
    return render_template('index.html')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    # Blueprint
    app.register_blueprint(Exchange.main, url_prefix='/api/exchanges')

    #app.register_error_handler(404, pagina_no_encontrada)
    app.run()
