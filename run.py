# RESPONSÁVEL APENAS PELA EXECUÇÃO DO SERVIDOR

from src.app import create_app

app = create_app()

if __name__ == '__main__':
    # Só roda isso localmente
    app.run(debug=True)
