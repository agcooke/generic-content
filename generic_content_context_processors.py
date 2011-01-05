from generic_content.models import GenericContent
def generic_content(request):
    try:
        generic_content = GenericContent.objects.get(def_url=request.path);
    except GenericContent.DoesNotExist:
        generic_content = None
    return {'generic_content':generic_content}


