import datetime


def convert_price(text):
  if "Contact for Price" in text or "Negotiable" in text:
    return -1
  price = ''.join(filter(str.isdigit, text))
  return int(price)

def convert_date(text):
  if "minute" in text:
    return datetime.date.today()

  if "an hour ago" in text:
    return datetime.date.today()

  if "a day ago" in text:
    return datetime.date.today() - datetime.timedelta(days=1)

  if "days" in text:
    days = int(''.join(filter(str.isdigit, text)))
    return datetime.date.today() - datetime.timedelta(days=days)

  if "a month ago" in text:
    return datetime.date.today() - datetime.timedelta(days=30)

  if "hours" in text:
    hours = int(''.join(filter(str.isdigit, text)))
    if datetime.datetime.now().hour > hours:
      return datetime.date.today()
    else:
      return datetime.date.today() - datetime.timedelta(days=1)

  if "months" in text:
    months = int(''.join(filter(str.isdigit, text)))
    return datetime.date.today() - datetime.timedelta(days=30*months)

def convert_views(text):
  views = int(''.join(filter(str.isdigit, text)))
  return views
