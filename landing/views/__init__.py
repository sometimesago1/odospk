#Views auto-detection module
#Import all auto-detectional views for visibility in urls.py
from .HomePage import HomePage
from .DirectionsPage import DirectionsPage
from .CoursesPage import CoursesPage

#List all imported views to send them to urls.py
__all__ = [
    'HomePage',
    'DirectionsPage',
    'CoursesPage'
]