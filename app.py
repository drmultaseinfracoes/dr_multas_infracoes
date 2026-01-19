from flask import Flask, render_template, send_file
from io import BytesIO
import csv
from datetime import datetime

def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return render_template("home.html", active="home")

    @app.get("/sobre")
    def sobre():
        return render_template("sobre.html", active="sobre")

    @app.get("/servicos")
    def servicos():
        return render_template("servicos.html", active="servicos")

    @app.get("/portfolio")
    def portfolio():
        return render_template("portfolio.html", active="portfolio")

    @app.get("/blog")
    def blog():
        return render_template("blog.html", active="blog")

    @app.get("/contato")
    def contato():
        return render_template("contato.html", active="contato")

    # Exemplo de "gerar arquivo de download" dinamicamente (CSV)
    @app.get("/download/relatorio.csv")
    def download_relatorio():
        output = BytesIO()
        writer = csv.writer(output)
        writer.writerow(["gerado_em", datetime.now().isoformat()])
        writer.writerow(["item", "valor"])
        writer.writerow(["visitas", 123])
        writer.writerow(["leads", 7])
        writer.writerow(["vendas", 2])

        output.seek(0)
        return send_file(
            output,
            as_attachment=True,
            download_name="relatorio.csv",
            mimetype="text/csv",
        )

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
