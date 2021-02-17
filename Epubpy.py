import os
from shutil import make_archive, rmtree


class Book:
    def __init__(self, title="title", genre="genre", description="description", author="author", editor="editor",
                 date="2000-01-01T16:00:00+00:00", isbn="ISBN"):

        root = os.getcwd()
        self.toc = ''
        self.content = ''
        self.folder = os.path.join(root, f"{title}")
        self.chapters = []

        self.language = 'en'
        self.title = title
        self.genre = genre
        self.description = description
        self.author = author
        self.editor = editor
        self.date = date
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

    # Folder structure preparation
    def preparation(self):
        if os.path.exists(os.path.join(os.getcwd(), f"{self.title}.epub")):
            os.remove(os.path.join(os.getcwd(), f"{self.title}.epub"))
        if os.path.exists(self.folder):
            rmtree(self.folder)

        os.makedirs(self.folder)
        os.makedirs(self.folder + r"\META-INF")
        os.makedirs(self.folder + r"\OPS")
        with open(self.folder + r"\META-INF\container.xml", 'w', encoding="UTF-8") as file:
            file.write(self.container)
        with open(self.folder + r"\mimetype", 'w', encoding="UTF-8") as file:
            file.write(self.mimetype)
        with open(self.folder + r"\stylesheet.css", 'w', encoding="UTF-8") as file:
            file.write(self.stylesheet)
        with open(self.folder + r"\toc.ncx", "w", encoding="UTF-8")as file:
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
                                <text>{self.title}</text>\n
                            </docTitle>\n
                            <navMap>\n''')
        with open(self.folder + r"\content.opf", 'w', encoding="UTF-8") as file:
            file.write(f'''<?xml version='1.0' encoding='utf-8'?>
                        <package xmlns="http://www.idpf.org/2007/opf" version="2.0" unique-identifier="uuid_id">\n
                            <metadate xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:opf="http://www.idpf.org/2007/opf" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:calibre="http://calibre.kovidgoyal.net/2009/metadate" xmlns:dc="http://purl.org/dc/elements/1.1/">\n
                                <dc:publisher>{self.editor}</dc:publisher>\n
                                <dc:description>{self.description}</dc:description>\n
                                <dc:language>{self.language}</dc:language>\n
                                <dc:create_epubtor opf:file-as="{self.author}" opf:role="aut">{self.author}</dc:create_epubtor>\n
                                <meta name="calibre:timestamp" content="{self.date}"/>\n
                                <dc:title>{self.title}</dc:title>\n
                                <meta name="cover" content="cover"/>\n
                                <dc:date>{self.date}</dc:date>\n
                                <dc:contributor opf:role="bkp">Epubpy</dc:contributor>\n
                                <dc:identifier opf:scheme="ISBN">{self.isbn}</dc:identifier>\n
                                <dc:identifier id="uuid_id" opf:scheme="uuid">UUID</dc:identifier>\n
                                <dc:subject>{self.genre}</dc:subject>\n
                                </metadate>\n
                                <manifest>\n
                                <item href="stylesheet.css" id="css" media-type="text/css"/>\n
                                <item href="toc.ncx" id="ncx" media-type="application/x-dtbncx+xml"/>\n''')

    def add_chapter(self, title='', capitolo=''):
        self.chapters.append((title, capitolo))

    def merge_chapters(self, chapter_list=None):
        if not chapter_list:
            chapter_list = self.chapters
        self.preparation()
        counter = 1000
        content = open(self.folder + r"\content.opf", 'a', encoding="UTF-8")
        toc = open(self.folder + r"\toc.ncx", 'a', encoding="UTF-8")
        for i in chapter_list:
            counter += 1
            toc.write(f'''<navPoint class="chapter" id="{counter}" playOrder="{counter}">
                   <navLabel>
                   <text>{i[0]}</text>
                    </navLabel>
                    <content src="OPS/{i[0]}.html"/>
                    </navPoint>\n''')
            content.write(f'<item href="OPS/{i[0]}.html" id="{counter}" media-type="application/xhtml+xml"/>\n')
            with open(self.folder + rf"\OPS\{i[0]}.html", 'w', encoding="UTF-8") as file:
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
        counter = 1000
        for _ in chapter_list:
            counter += 1
            content.write(f'<itemref idref="{counter}"/>\n')
        content.write('</spine>\n</package>\n')
        toc.write("</navMap>\n</ncx>")
        toc.close()
        content.close()

    def create_epub(self):
        make_archive(os.path.join(os.getcwd(), f"{self.title}"), 'zip', self.folder)
        os.chdir(os.getcwd())
        os.rename(f"{self.title}.zip", f"{self.title}.epub")
        rmtree(self.folder, ignore_errors=True)
