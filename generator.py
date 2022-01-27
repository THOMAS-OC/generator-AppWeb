import os



reset_code = """
/* http://meyerweb.com/eric/tools/css/reset/ 
   v2.0 | 20110126
   License: none (public domain)
*/

html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section {
	display: block;
}
body {
	line-height: 1;

}
ol, ul {
	list-style: none;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}"""


name_doc_html = input("Nom du document ? ('Document' par défaut) : \n")
if name_doc_html :
    html_code = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles/reset.css">
        <link rel="stylesheet" href="styles/style.css">
        <script defer src="scripts/script.js"></script>
        <title>{name_doc_html}</title>
    </head>
    <body>
        
    </body>
    </html>"""
else :
    html_code = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles/reset.css">
        <link rel="stylesheet" href="styles/style.css">
        <script defer src="scripts/script.js"></script>
        <title>Document</title>
    </head>
    <body>
        
    </body>
    </html>"""

html = open("index.html", "w", encoding="utf-8")
html.write(html_code)
html.close()


# Création des dossiers
os.mkdir("styles")
os.mkdir("scripts")
os.mkdir("images")
os.mkdir("fonts")

# Création des fichiers style et script
os.chdir(r"C:\Users\Thomas\Desktop\generator-AppWeb\styles")

sass = open("style.scss", "w", encoding="utf-8")
sass.close()

reset = open("reset.css", "w", encoding="utf-8")
reset.write(reset_code)
reset.close()
os.chdir(r"C:\Users\Thomas\Desktop\generator-AppWeb\scripts")
script = open("script.js", "w", encoding="utf-8")
script.close()