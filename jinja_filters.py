import datetime


def event_time(event):
    start = event.date
    end = start + datetime.timedelta(hours=float(event.length))
    return '{} - {}'.format(start.strftime('%H:%M'), end.strftime('%H:%M'))


def strip_paragraph(text):
    return text.strip()[len('<p>'):-len('</p>')]
