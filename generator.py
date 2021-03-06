import os



#Création du dossier projet
os.chdir(r"C:\Users\Thomas\Desktop")
name_folder_project = input("Comment voulez-vous nommer votre projet ?")
if name_folder_project :
    os.mkdir(name_folder_project)
else :
    os.mkdir("APP_FRONT-END")
    name_folder_project = "APP_FRONT-END"


# On se place dans le dossier crée
os.chdir(r"C:\Users\Thomas\Desktop\{}".format(name_folder_project))

package_code = """{
  "name": "nouveau-dossier",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "sass": "sass --watch styles/style.scss:styles/style.css"
  },
  "author": "",
  "license": "ISC"
}
"""


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
git = open(".gitignore", "w", encoding="utf-8")
git.write("git.py\n*txt\nsass_generate.py")
git.close()

# Création des dossiers
os.mkdir("styles")
os.mkdir("scripts")
os.mkdir("images")
os.mkdir("fonts")

# Création des fichiers style et script
os.chdir(r"C:\Users\Thomas\Desktop\{}\styles".format(name_folder_project))
css_or_scss = int(input("Souhaitez-vous écrire du code sass ou bien du code css classique ? 1 : SASS 2 : CSS classique \n >>>  "))
if css_or_scss == 1 :
    css = open("style.scss", "w", encoding="utf-8")
    css.close()
    """On crée aussi le fichier css pour qu'il soit suivi par git ! """
    css = open("style.css", "w", encoding="utf-8")
    css.close()
    os.chdir(r"C:\Users\Thomas\Desktop\{}".format(name_folder_project))
    package = open("package.json", "w", encoding="utf-8")
    package.write(package_code)
    package.close()
elif css_or_scss == 2 :
    css = open("style.css", "w", encoding="utf-8")
    css.close()
else :
    css = open("style.scss", "w", encoding="utf-8")
    css.close()

os.chdir(r"C:\Users\Thomas\Desktop\{}\styles".format(name_folder_project))
reset = open("reset.css", "w", encoding="utf-8")
reset.write(reset_code)
reset.close()

os.chdir(r"C:\Users\Thomas\Desktop\{}\scripts".format(name_folder_project))
script = open("script.js", "w", encoding="utf-8")
script.close()

#Versionning
os.chdir(r"C:\Users\Thomas\Desktop\{}".format(name_folder_project))

versionning = int(input("Voulez-vous versionner ce projet ? 1 : OUI 2 : NON \n >>>  "))
if versionning == 1 :
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "Structure du projet mise en place" ')

else :
    pass

#Lancement de VS code
open_vs_code = int(input("Voulez-vous ourvir le projet dans VScode ? 1 : OUI 2 : NON \n >>>  "))
if open_vs_code == 1 :
    os.chdir(r"C:\Users\Thomas\Desktop\{}".format(name_folder_project))
    os.system("code .")
    os.system("code index.html")
    
    if css_or_scss == 2 :
        os.system("code styles/style.css")
        os.system("code scripts/script.js")

    elif css_or_scss == 1 :
        os.system("code styles/style.scss")
        os.system("code scripts/script.js")
        sass_py = open("sass_generate.py", "w", encoding="utf-8")
        sass_py.write("import os\nos.system('npm run sass')")
        sass_py.close()
        os.system("npm run sass")
    else :
        pass
else :
    pass

