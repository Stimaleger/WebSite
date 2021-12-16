from django.template import loader
from django.http import HttpResponse
from django.conf import settings
from weasyprint import HTML, CSS
import io


def curriculum(request):
    template = loader.get_template('curriculum/curriculum.html')
    context = {}
    return HttpResponse(template.render(context, request))


def generate_pdf(request):
    """Generate pdf."""
    buffer = io.BytesIO()
    # Rendered
    html_string = loader.render_to_string('curriculum/curriculum.html')
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
        result = html.write_pdf(presentational_hints=True, stylesheets=[CSS(settings.STATIC_ROOT)])

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'filename=list_people.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    buffer.write(result)
    buffer.seek(0)
    response.write(buffer.read())
    # with tempfile.NamedTemporaryFile(delete=True) as output:
    #     output.write(result)
    #     output.flush()
    #     output = open(output.name, 'r')
    #     response.write(output.read())
    return response
