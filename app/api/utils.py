from app.models import Report
from flask import current_app


def convert_report_dict(report_dict):
    tmp = Report(report_dict['count'], report_dict['total'], report_dict['currency'])
    current_app.logger.debug("tmp is {}".format(tmp))
    return tmp


def convert_report_json_2_object(json_list):

    report_list = [ convert_report_dict(item) for item in json_list ]

    return report_list

def add_to_dict_if_form_field_exist(one_dict, dict_key, form_field, is_integer=False):

    if form_field != '':
        if is_integer:
            one_dict[dict_key] = int(form_field)
        else:
            one_dict[dict_key] = form_field

    return one_dict