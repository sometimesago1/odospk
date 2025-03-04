#Views auto-detection module
#Import all auto-detectional views for visibility in urls.py
from .HomePage import HomePage

#List all imported views to send them to urls.py
__all__ = [
    'HomePage',
]