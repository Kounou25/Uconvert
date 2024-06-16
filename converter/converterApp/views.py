from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from pdf2docx import Converter
import tempfile
import os
from io import BytesIO

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']

            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                temp_pdf.write(pdf_file.read())
                temp_pdf_path = temp_pdf.name

            with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_docx:
                temp_docx_path = temp_docx.name

            cv = Converter(temp_pdf_path)
            cv.convert(temp_docx_path, start=0, end=None)
            cv.close()

            with open(temp_docx_path, 'rb') as docx_file:
                docx_io = BytesIO(docx_file.read())

            docx_io.seek(0)
            os.remove(temp_pdf_path)
            os.remove(temp_docx_path)

            response = HttpResponse(docx_io, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename={pdf_file.name.replace(".pdf", ".docx")}'

            return response
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})
