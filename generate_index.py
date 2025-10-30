import os

ARTISTAS_DIR = "artistas"
ALBUNS_DIR = "albuns"
GENEROS_DIR = "generos"
OUTPUT_FILE = "index.html"

def gerar_card(nome, pasta):
    slug = nome.replace(".html", "")
    titulo = slug.replace("-", " ").title()
    imagem = f"assets/img/{slug}.jpg"
    return f"""
    <div class="album-card">
      <a href="{pasta}/{nome}">
        <img src="{imagem}" alt="{titulo}" />
        <h3>{titulo}</h3>
      </a>
    </div>
    """

def gerar_menu_generos():
    generos = sorted(os.listdir(GENEROS_DIR))
    lista = ""
    for genero in generos:
        nome = genero.replace(".html", "").title()
        lista += f'<li><a href="generos/{genero}">{nome}</a></li>\n'
    return lista

def main():
    artistas = sorted(os.listdir(ARTISTAS_DIR))[-5:]
    albuns = sorted(os.listdir(ALBUNS_DIR))[-5:]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Arquivo Sonoro</title>
  <link rel="stylesheet" href="assets/css/style.css" />
</head>
<body>
  <header>
    <h1>ARQUIVO SONORO</h1>
    <div class="search-bar">
      <input type="text" placeholder="Buscar artista ou álbum..." />
    </div>
  </header>
  <div class="content">
    <section class="latest-updates">
""")
        for nome in artistas:
            f.write(gerar_card(nome, ARTISTAS_DIR))
        for nome in albuns:
            f.write(gerar_card(nome, ALBUNS_DIR))

        f.write("""
    </section>
    <aside class="genres-menu">
      <h4>Gêneros</h4>
      <ul>
""")
        f.write(gerar_menu_generos())
        f.write("""
      </ul>
    </aside>
  </div>
</body>
</html>
""")

if __name__ == "__main__":
    main()
