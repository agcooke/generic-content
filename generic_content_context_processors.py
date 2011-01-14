from generic_content.models import GenericContent
def generic_content(request,path=None):
    try:
        if path == None:
            if request.path == '':
                path = '/'
            else:
                path = request.path
        generic_content = GenericContent.objects.get(def_url=path);
    except GenericContent.DoesNotExist:
        generic_content = None
    return {'generic_content':generic_content}


