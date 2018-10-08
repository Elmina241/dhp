import os, sys
# место, где лежит джанго
sys.path.append('/usr/local/lib/python2.7/dist-packages/django/')
# место, где лежит проект
sys.path.append('/home/web/dhp/dhp/')
# файл конфигурации проекта
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_example.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
