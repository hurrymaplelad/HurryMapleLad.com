from datetime import date
from core import RequestHandler

class Experiment(RequestHandler):
  title = 'Nameless Experiment'
  slug = 'experiment'
  date = date.today()
  tags = ()

  def render(self, data={}):
    data.update({
      'experiment': self
    })
    path = 'templates/experiments/%s.html' % self.slug
    super(Experiment, self).render(path, data)

  def get(self):
    self.render()

class IsoBots(Experiment):
  title = 'Isometric Robots'
  slug = 'isobots'
  date = date(2004, 1, 1)
  tags = 'flash',

class MiniGolf(Experiment):
  title = 'Mini Golf'
  slug = 'minigolf'
  date = date(2004, 1, 1)
  tags = 'flash',

class NinjaSlug(Experiment):
  title = 'Ninja Slug'
  slug = 'ninjaslug'
  date = date(2004, 1, 1)
  tags = 'flash',

class Pirate(Experiment):
  title = 'Pirates!'
  slug = 'pirate'
  date = date(2004, 1, 1)
  tags = 'flash',

class RotationalGrazing(Experiment):
  title = 'Rotational Grazing'
  slug = 'rotationalgrazing'
  date = date(2008, 9, 1)
  tags = 'flash',

class SpaceShmup(Experiment):
  title = 'Space Shoot \'em Up'
  slug = 'spaceshmup'
  date = date(2003, 10, 1)
  tags = 'flash',

class Tank(Experiment):
  title = 'Tank'
  slug = 'tank'
  date = date(2004, 1, 1)
  tags = 'flash',

class Tetris(Experiment):
  title = 'Tetris'
  slug = 'tetris'
  date = date(2004, 1, 1)
  tags = 'flash',

class Throwing(Experiment):
  title = 'Throwing'
  slug = 'throwing'
  date = date(2004, 1, 1)
  tags = 'flash',

class TowerDefense(Experiment):
  title = 'Tower Defense'
  slug = 'towerdefense'
  date = date(2004, 1, 1)
  tags = 'flash',

class TurtleShmup(Experiment):
  title = 'Turtle Shoot \'em Up'
  slug = 'turtleshmup'
  date = date(2004, 1, 1)
  tags = 'flash',

