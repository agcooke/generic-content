import logging
import re

from django import template
from generic_content.models import GenericContent
register = template.Library()

class GenericContentNode(template.Node):
    def __init__(self, var_name, current_url):
        self.current_url = current_url
        self.var_name = var_name
    def render(self, context):
        if self.current_url[0] != '/':
            self.current_url = '/'+self.current_url
        context[self.var_name] = GenericContent.objects.get(def_url=self.current_url)
        return ''

@register.tag
def generic_content(parser, token):
    logging.debug(token)
    # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%r tag had invalid arguments" % tag_name
    current_url,var_name = m.groups()
    logging.debug(var_name+' -- '+current_url)
    return GenericContentNode(var_name,current_url)
