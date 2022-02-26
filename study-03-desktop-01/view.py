import eel
import desktop
import search

# import sys
# import os

app_name = "html"
end_point = "index.html"
size = (700, 600)


@ eel.expose
def kimetsu_search(word, csv_name):
    search.kimetsu_search(word, csv_name)


desktop.start(app_name, end_point, size)
# desktop.start(size=size,appName=app_name,endPoint=end_point)


# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     base_path = getattr(sys, '_MEIPASS', os.path.dirname(
#         os.path.abspath(__file__)))
#     return os.path.join(base_path, relative_path)


# os.popen(resource_path('view'))
