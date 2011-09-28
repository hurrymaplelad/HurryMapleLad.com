from google.appengine.ext.webapp import template
from datetime import datetime
from dateutil.relativedelta import relativedelta

register = template.create_template_register()

@register.filter
def datedelta(value):
  delta = relativedelta(datetime.utcnow(), value)
  if delta.years >= 1:
    return '%s year%s ago' % (
      delta.years,
      's' if delta.years > 1 else ''
    )
  if delta.months >= 1:
    return '%s month%s ago' % (
      delta.months,
      's' if delta.months > 1 else '',
    )
  if delta.days >= 7:
    weeks = math.floor(delta.days / 7)
    return '%s week%s ago' % (
      weeks,
      's' if weeks > 1 else '',
    )
  if delta.days > 1:
    return '%s days ago' % delta.days
  if delta.days == 1:
    return 'yesterday'
  else:
    return 'today'

