try:
    VERSION = __import__('pkg_resources') \
        .get_distribution(__name__).version
except:
    VERSION = '0.0.3'
