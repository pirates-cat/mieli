import copy

def clean_options(options):
    opts = copy.copy(options)
    del opts['pythonpath']
    del opts['settings']
    del opts['verbosity']
    del opts['traceback']
    del opts['no_color']
    return opts
