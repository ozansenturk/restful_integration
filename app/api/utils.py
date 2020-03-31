from app.models import Report, FxMerchant, CustomerInfoBase, Acquirer, TransactionQuery, MerchantBase, Merchant
from flask import current_app


def convert_report_dict(report_dict):
    tmp = Report(report_dict['count'], report_dict['total'], report_dict['currency'])
    current_app.logger.debug("tmp is {}".format(tmp))
    return tmp


def convert_report_json_2_object_list(json_list):

    report_list = [ convert_report_dict(item) for item in json_list ]

    return report_list


def add_to_dict_if_form_field_exist(one_dict, dict_key, form_field, is_integer=False):

    if form_field != '':
        if is_integer:
            one_dict[dict_key] = int(form_field)
        else:
            one_dict[dict_key] = form_field

    return one_dict


def convert_fx_merchant_dict(merchant_dict):
    tmp = FxMerchant(merchant_dict['originalAmount'], merchant_dict['originalCurrency'])
    current_app.logger.debug("FxMerchant is {}".format(tmp))
    return tmp


def convert_customer_info_base_dict(customer_info_base_dict):
    tmp = CustomerInfoBase(customer_info_base_dict['number'], customer_info_base_dict['email'],
                     customer_info_base_dict['billingFirstName'], customer_info_base_dict['billingLastName'])
    current_app.logger.debug("CustomerInfoBase is {}".format(tmp))
    return tmp


def convert_merchant_base_dict(merchant_base_dict):
    tmp = MerchantBase(merchant_base_dict['id'], merchant_base_dict['name'])
    current_app.logger.debug("MerchantBase is {}".format(tmp))
    return tmp


def convert_merchant_dict(merchant_dict):
    tmp = Merchant(merchant_dict['referenceNo'], merchant_dict['status'],
                     merchant_dict['operation'], merchant_dict['message'], merchant_dict['created_at']
                     , merchant_dict['transactionId'])
    current_app.logger.debug("Merchant is {}".format(tmp))
    return tmp


def convert_acquirer_dict(acquirer_dict):
    tmp = Acquirer(acquirer_dict['id'], acquirer_dict['name'],
                     acquirer_dict['code'], acquirer_dict['type'])
    current_app.logger.debug("Acquirer is {}".format(tmp))
    return tmp


def initialize_transaction_query_with_dict(transaction_query_dict):

    tmp = TransactionQuery(transaction_query_dict)

    current_app.logger.debug("TransactionQuery is {}".format(tmp))
    return tmp


def convert_transaction_query_json_2_object_list(transaction_query_dict_list):

    query_list = [initialize_transaction_query_with_dict(transaction_query_dict)
                  for transaction_query_dict in transaction_query_dict_list]

    return query_list


def extract_page_number(url_str):
    index = url_str.find("page=")

    page_num = url_str[index+5:]
    current_app.logger.debug("Page Number is {}".format(page_num))

    return page_num