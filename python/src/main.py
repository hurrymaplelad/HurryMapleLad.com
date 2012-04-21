"""
Update source and libs to python module path.
"""
import os
import sys
dirname = os.path.dirname(__file__)
libs_dir = os.path.join(os.path.split(dirname)[0], 'libs')
sys.path.insert(0, libs_dir)
sys.path.insert(1, dirname)

import inspect
import experiments

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from core import RequestHandler

#TODO: move this to __all__
experimentControllers = [e for name, e in inspect.getmembers(
  experiments, 
  lambda(o): 
    inspect.isclass(o) 
    and issubclass(o, experiments.Experiment)
    and o is not experiments.Experiment
)]

# sort by entry date
experimentControllers.sort(
  key = lambda e: e.date, 
  reverse = True
)

class Experiments(RequestHandler):
  def get(self):
    self.render('../../templates/experiments.html', {
      'experiments': experimentControllers
    })

application = webapp.WSGIApplication([
    ('/', Experiments),
  ]+[
    ('/%s/' % e.slug, e) for e in experimentControllers
  ],
  debug=True
)

if __name__ == "__main__":
  run_wsgi_app(application)
