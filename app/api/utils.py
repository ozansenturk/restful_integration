from app.models import Report, FxMerchant, CustomerInfoBase, Acquirer, TransactionQuery, MerchantBase, Merchant
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


def convert_transaction_query_dict(transaction_query_dict):
    tmp = TransactionQuery(transaction_query_dict['fx'], transaction_query_dict['customerInfo'],
                     transaction_query_dict['merchant'], transaction_query_dict['ipn']['sent'],
                transaction_query_dict['transaction'], transaction_query_dict['acquirer']
                           , transaction_query_dict['refundable'])

    current_app.logger.debug("TransactionQuery is {}".format(tmp))
    return tmp