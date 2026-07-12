from pypdf import PdfReader
import tempfile


def extract_pdf_text(file_content):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp:

        temp.write(file_content)

        path=temp.name


    reader=PdfReader(path)


    text=""


    for page in reader.pages:

        extracted=page.extract_text()

        if extracted:

            text+=extracted+"\n"


    return text