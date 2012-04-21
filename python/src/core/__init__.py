
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

template.register_template_library('core.filters')

class RequestHandler(webapp.RequestHandler):
  def render(self, path, data={}):
    self.response.out.write(template.render(path, data))
