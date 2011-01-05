from generic_content.models import GenericContent

from django import template
from freewanderer.utils.utils import setup_logging
logger = setup_logging()
register = template.Library()

class GenericContentNode(template.Node):
    def __init__(self, var_name, current_url):
        self.current_url = current_url
        self.var_name = var_name
    def render(self, context):
        context[self.var_name] = GenericContent.objects.get(def_url=self.current_url)
        return ''

import re
#@register.tag
@register.tag
def generic_content(parser, token):
    # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%r tag had invalid arguments" % tag_name
    var_name,current_url = m.groups()
    return GenericContentNode(var_name,current_url)
