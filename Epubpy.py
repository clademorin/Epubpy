import os
from shutil import make_archive, rmtree


class Book:
    def __init__(self, titolo="Titolo", genere="Genere", descrizione="Descrizione", autore="Autore", editore="Editore",
                 data="2000-01-01T16:00:00+00:00", isbn="ISBN"):

        root = os.getcwd()
        self.toc = ''
        self.content = ''
        self.cartella = os.path.join(root, f"{titolo}")
        self.capitoli = []

        self.language = 'en'
        self.titolo = titolo
        self.genere = genere
        self.descrizione = descrizione
        self.autore = autore
        self.editore = editore
        self.data = data
        self.isbn = isbn
        self.mimetype = "application/epub+zip"
        self.container = '''<?xml version="1.0"?>
                    <container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
                        <rootfiles>
                            <rootfile full-path="content.opf" media-type="application/oebps-package+xml"/>

                        </rootfiles>
                    </container>
                    '''
        self.stylesheet = '''@namespace h "http://www.w3.org/1999/xhtml";
                    .CCurrentAndItalic {
                        font-style: italic
                    }
                    .PBodyTextFirstIndent {
                        display: block;
                        font-family: "Times New Roman", serif;
                        font-size: 1em;
                        margin-bottom: 0.8em;
                        margin-left: 0;
                        margin-right: 0;
                        margin-top: 0;
                        text-indent: 1.2em
                    }
                    .PHeading {
                        display: block;
                        font-family: "Times New Roman", serif;
                        font-size: 1em;
                        font-weight: bold;
                        margin-bottom: 0.8em;
                        margin-left: 0;
                        margin-right: 0;
                        margin-top: 0;
                        text-align: center;
                        text-indent: 0
                    }
                    .PHeading1 {
                        display: block;
                        font-family: "Times New Roman", serif;
                        font-size: 1.41667em;
                        font-weight: bold;
                        margin-bottom: 1.2em;
                        margin-left: 0;
                        margin-right: 0;
                        margin-top: 0;
                        text-align: center;
                        text-indent: 0
                    }
                    .PHeading2 {
                        display: block;
                        font-family: "Times New Roman", serif;
                        font-size: 1.125em;
                        font-weight: bold;
                        margin-bottom: 1.2em;
                        margin-left: 0;
                        margin-right: 0;
                        margin-top: 0;
                        text-align: center;
                        text-indent: 0
                    }
                    .PHeading3 {
                        display: block;
                        font-family: "Times New Roman", serif;
                        font-size: 1em;
                        font-weight: bold;
                        margin-bottom: 0.8em;
                        margin-left: 0;
                        margin-right: 0;
                        margin-top: 0;
                        text-indent: 0
                    }
                    .calibre {
                        display: block;
                        font-size: 1em;
                        margin-bottom: 0;
                        margin-left: 5pt;
                        margin-right: 5pt;
                        margin-top: 0;
                        padding-left: 0;
                        padding-right: 0;
                        page-break-before: always
                    }
                    .calibre1 {
                        font-size: 1.41176em
                    }
                    .calibre2 {
                        display: block
                    }'''

    def preparazione(self):
        if os.path.exists(os.path.join(os.getcwd(), f"{self.titolo}.epub")):
            os.remove(os.path.join(os.getcwd(), f"{self.titolo}.epub"))
        if os.path.exists(self.cartella):
            rmtree(self.cartella)

        os.makedirs(self.cartella)
        os.makedirs(self.cartella + r"\META-INF")
        os.makedirs(self.cartella + r"\OPS")
        with open(self.cartella + r"\META-INF\container.xml", 'w', encoding="UTF-8") as file:
            file.write(self.container)
        with open(self.cartella + r"\mimetype", 'w', encoding="UTF-8") as file:
            file.write(self.mimetype)
        with open(self.cartella + r"\stylesheet.css", 'w', encoding="UTF-8") as file:
            file.write(self.stylesheet)
        with open(self.cartella + r"\toc.ncx", "w", encoding="UTF-8")as file:
            file.write(f'''<?xml version='1.0' encoding='utf-8'?>\n
                        <ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1" xml:lang="en">\n
                            <head>\n
                                <meta content="9aa41227-53c3-44e0-ad66-0bfc5e888543" name="dtb:uid"/>\n
                                <meta content="2" name="dtb:depth"/>\n
                                <meta content="Epubpy" name="dtb:generator"/>\n
                                <meta content="0" name="dtb:totalPageCount"/>\n
                                <meta content="0" name="dtb:maxPageNumber"/>\n
                            </head>\n
                            <docTitle>\n
                                <text>{self.titolo}</text>\n
                            </docTitle>\n
                            <navMap>\n''')
        with open(self.cartella + r"\content.opf", 'w', encoding="UTF-8") as file:
            file.write(f'''<?xml version='1.0' encoding='utf-8'?>
                        <package xmlns="http://www.idpf.org/2007/opf" version="2.0" unique-identifier="uuid_id">\n
                            <metadata xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:opf="http://www.idpf.org/2007/opf" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:calibre="http://calibre.kovidgoyal.net/2009/metadata" xmlns:dc="http://purl.org/dc/elements/1.1/">\n
                                <dc:publisher>{self.editore}</dc:publisher>\n
                                <dc:description>{self.descrizione}</dc:description>\n
                                <dc:language>{self.language}</dc:language>\n
                                <dc:creator opf:file-as="{self.autore}" opf:role="aut">{self.autore}</dc:creator>\n
                                <meta name="calibre:timestamp" content="{self.data}"/>\n
                                <dc:title>{self.titolo}</dc:title>\n
                                <meta name="cover" content="cover"/>\n
                                <dc:date>{self.data}</dc:date>\n
                                <dc:contributor opf:role="bkp">Epubpy</dc:contributor>\n
                                <dc:identifier opf:scheme="ISBN">{self.isbn}</dc:identifier>\n
                                <dc:identifier id="uuid_id" opf:scheme="uuid">UUID</dc:identifier>\n
                                <dc:subject>{self.genere}</dc:subject>\n
                                </metadata>\n
                                <manifest>\n
                                <item href="stylesheet.css" id="css" media-type="text/css"/>\n
                                <item href="toc.ncx" id="ncx" media-type="application/x-dtbncx+xml"/>\n''')

    def aggiungi_capitoli(self, titolo='', capitolo=''):
        self.capitoli.append((titolo, capitolo))

    def unisci_capitoli(self, lista=None):

        if not lista:
            lista = self.capitoli
        self.preparazione()
        contatore = 1000
        content = open(self.cartella + r"\content.opf", 'a', encoding="UTF-8")
        toc = open(self.cartella + r"\toc.ncx", 'a', encoding="UTF-8")
        for i in lista:
            contatore += 1
            toc.write(f'''<navPoint class="chapter" id="{contatore}" playOrder="{contatore}">
                   <navLabel>
                   <text>{i[0]}</text>
                    </navLabel>
                    <content src="OPS/{i[0]}.html"/>
                    </navPoint>\n''')
            content.write(f'<item href="OPS/{i[0]}.html" id="{contatore}" media-type="application/xhtml+xml"/>\n')
            with open(self.cartella + rf"\OPS\{i[0]}.html", 'w', encoding="UTF-8") as file:
                file.write(f'''<?xml version='1.0' encoding='utf-8'?>
                    <html xmlns="http://www.w3.org/1999/xhtml">
                        <head>
                            <title>{i[0]}</title>
                            <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
                            <link href="../stylesheet.css" rel="stylesheet" type="text/css"/>
                        </head>
                    <body>
                        <h1>{i[0]}</h1>
                        {str(i[1])}
                    </body>
                    </html>''')
        content.write('''</manifest>\n<spine toc="ncx">\n''')
        contatore = 1000
        for i in lista:
            contatore += 1
            content.write(f'<itemref idref="{contatore}"/>\n')
        content.write('</spine>\n</package>\n')
        toc.write("</navMap>\n</ncx>")
        toc.close()
        content.close()

    def crea(self):

        make_archive(os.path.join(os.getcwd(), f"{self.titolo}"), 'zip', self.cartella)
        os.chdir(os.getcwd())
        os.rename(f"{self.titolo}.zip", f"{self.titolo}.epub")
        rmtree(self.cartella, ignore_errors=True)
