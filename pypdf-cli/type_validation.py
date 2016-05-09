from __future__ import print_function
import argparse

def validate_extract_pages(from_page, to_page):
    if not isinstance(from_page, int) or not isinstance(to_page, int):
        return_dict = {'check': False, 'message': 'Page numbers must be integers'}
    elif from_page < 0 or to_page < 0:
        return_dict = {'check': False, 'message': 'Page numbers must be positive integers'}
    elif (from_page > to_page) and to_page != 0:
        return_dict = {'check': False, 'message': 'initial page must be smaller than final page'}
    else:
        return_dict = {'check':True, 'message': ''}

    validation_result(return_dict)
    return

def validation_result(return_dict):
    if not return_dict['check']:
        raise argparse.ArgumentTypeError(return_dict['message'])
    return
