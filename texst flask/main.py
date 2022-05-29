from app.main import create_app


app = create_app()


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 2000
    app.run(host=host, port=port, debug=True)
