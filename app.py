# RESPONSÁVEL APENAS PELA EXECUÇÃO DO SERVIDOR

from src.app import create_app

app = create_app()
app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)