import logging

def my_function():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')


my_function()

>>>
ERROR:root:Error log here
