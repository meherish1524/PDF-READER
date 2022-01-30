import PyPDF2
import pyttsx3


class app:
    path = open('s4.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(path)
    print(pdfReader.numPages)
    from_page = pdfReader.getPage(1)
    text = from_page.extractText()
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()
