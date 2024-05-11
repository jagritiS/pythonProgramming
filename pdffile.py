from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from io import StringIO
from spacy.matcher import Matcher
import spacy

# Load the spacy model and create the matcher with the patterns
nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)
method_pattern = [{"LOWER": "methods"}, {"OP": "?"}]
material_pattern = [{"LOWER": "materials"}, {"OP": "?"}]
mm_pattern = [{"LOWER": "methods"}, {"LOWER": "and"}, {"LOWER": "materials"}]
methodology_pattern = [{"LOWER": "methodology"}]
am_pattern = [{"LOWER": "materials"}, {"LOWER": "and"}, {"LOWER": "methods"}]
m_pattern = [{"LOWER": "material"}, {"LOWER": "and"}, {"LOWER": "method"}]
ms_pattern = [{"LOWER": "materials"}, {"LOWER": "and"}, {"LOWER": "methods"}]
pattern_list = [method_pattern, material_pattern, mm_pattern, methodology_pattern, am_pattern, m_pattern, ms_pattern]
for pattern in pattern_list:
    matcher.add("MaterialMethods", [pattern])
# Open the PDF file
with open('example.pdf', 'rb') as file:

    # Create a PDF parser object
    parser = PDFParser(file)

    # Create a PDF document object
    document = PDFDocument(parser)

    # Get the outlines
    outlines = document.get_outlines()

    # Find the level 1 outline item with the material/methods pattern
    material_methods_outline = None
    for level, title, dest, a, se in outlines:
        if level == 1:
            doc = nlp(title.lower())
            matches = matcher(doc)
            if matches:
                material_methods_outline = (level, title, dest, a, se)
                break
# Extract the text until the next level 1 outline item
    if material_methods_outline is not None:
        _, material_methods_title, material_methods_dest, _, _ = material_methods_outline
        output_string = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output_string, laparams=None)
        interpreter = PDFPageInterpreter(manager, converter)

        for page in PDFPage.get_pages(file):
            interpreter.process_page(page)
            text = output_string.getvalue()
            if material_methods_title in text:
                text = text.split(material_methods_title)[-1]
                output_string = StringIO(text)
            elif '\n1 ' in text:
                # Found another level 1 outline item, stop extracting
                break

        # Print the extracted text
        print(output_string.getvalue())
