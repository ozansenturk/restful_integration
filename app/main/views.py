from app.main import bp
from flask import render_template,request, url_for,current_app,flash, redirect, session
from app.main.forms import ReportForm, TransactionQueryForm, TransactionForm
from app.api import services
from flask import abort
from app.models import Report
from app.api import utils


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@bp.route('/report', methods=['GET', 'POST'])
def report():

    report_list=[]
    form = ReportForm()
    if form.validate_on_submit():

        data = {"fromDate": form.fromDate.data.strftime('%Y-%m-%d'), "toDate": form.toDate.data.strftime('%Y-%m-%d')}

        data = utils.add_to_dict_if_form_field_exist(data, 'acquirer', form.acquirer.data, True)
        data = utils.add_to_dict_if_form_field_exist(data, 'merchant', form.merchant.data, True)

        current_app.logger.debug("filter data for report is {}".format(data))

        response = services.post_query(current_app.config['REPORT_URL'], data)

        response_status = response['status']
        response_list = response['response']

        if len(response_list) == 0:
            current_app.logger.debug("no response_data found {}".format(response_list))
            abort(404)

        current_app.logger.debug("response from report url is {}".format(response))

        report_list = utils.convert_report_json_2_object_list(response_list)

    return render_template('report.html', form=form, reports=report_list)


@bp.route('/transaction_query/<page>', methods=['GET', 'POST'])
def transaction_query(page):

    next_url = prev_url = per_page = current_page = from_ = to_ = response = None

    transaction_query_list = []

    if request.method == 'GET' and int(page)>=1 :
        form = TransactionQueryForm(formdata=request.form)
        data = session['data']
        current_app.logger.debug("GET executed")
        response = services.post_query(current_app.config['TRANSACTION_QUERY_URL'],
                                       data, params={"page": page})

        response_list = response['data']

        if len(response_list) == 0:
            current_app.logger.debug("no transaction_query data found {}".format(response_list))
            abort(404)

        transaction_query_list = utils.convert_transaction_query_json_2_object_list(response_list)
        current_app.logger.debug("response from report url is {}".format(transaction_query_list))

        if "prev_page_url" in response and response["prev_page_url"] is not None:
            prev_url = "/transaction_query/" + utils.extract_page_number(response["prev_page_url"])

        if "next_page_url" in response and response["next_page_url"] is not None:
            next_url = "/transaction_query/" + \
                       utils.extract_page_number(response["next_page_url"])

        current_page = response['current_page']
        per_page = response['per_page']
        from_ = response['from']

    else:
        form = TransactionQueryForm()

    if request.method == 'POST' and form.validate_on_submit():

        data = {"fromDate": form.fromDate.data.strftime('%Y-%m-%d'), "toDate": form.toDate.data.strftime('%Y-%m-%d')}

        data = utils.add_to_dict_if_form_field_exist(data, 'status', form.status.data)
        data = utils.add_to_dict_if_form_field_exist(data, 'operation', form.operation.data)
        data = utils.add_to_dict_if_form_field_exist(data, 'merchantId', form.merchant.data, True)
        data = utils.add_to_dict_if_form_field_exist(data, 'acquirerId', form.acquirer.data, True)
        data = utils.add_to_dict_if_form_field_exist(data, 'paymentMethod', form.payment_method.data)
        data = utils.add_to_dict_if_form_field_exist(data, 'errorCode', form.error_code.data)
        data = utils.add_to_dict_if_form_field_exist(data, 'filterField', form.filter_field.data)
        data = utils.add_to_dict_if_form_field_exist(data, 'filterValue', form.filter_value.data)
        data = utils.add_to_dict_if_form_field_exist(data, 'page', form.page.data, True)

        session['data'] = data
        current_app.logger.debug("filter data for report is {}".format(data))

        response = services.post_query(current_app.config['TRANSACTION_QUERY_URL'], data)

        # current_app.logger.debug("response from report url is {}".format(response))

        response_list = response['data']

        if len(response_list) == 0:
            current_app.logger.debug("no transaction_query data found {}".format(response_list))
            abort(404)

        transaction_query_list = utils.convert_transaction_query_json_2_object_list(response_list)

        if "prev_page_url" in response and response["prev_page_url"] is not None:
            prev_url = "/transaction_query/"+utils.extract_page_number(response["prev_page_url"])

        if "next_page_url" in response and response["next_page_url"] is not None:
            next_url = "/transaction_query/"+\
                       utils.extract_page_number(response["next_page_url"])

        current_page = response['current_page']
        per_page = response['per_page']
        from_ = response['from']
        to_ = response['to']

    return render_template('transaction_query.html', form=form, transaction_queries=transaction_query_list,
                           next_url=next_url, prev_url=prev_url,
                           page=current_page, per_page=per_page)


@bp.route('/transaction', methods=['GET', 'POST'])
def transaction():

    transaction = None

    form = TransactionForm()
    if form.validate_on_submit():

        data = {"transactionId": form.transaction_id.data}

        current_app.logger.debug("filter data for transaction is {}".format(data))

        response = services.post_query(current_app.config['TRANSACTION_URL'], data)

        transaction = response['transaction']

        if transaction is None:
            current_app.logger.debug("no response_data found {}".format(transaction))
            abort(404)

        current_app.logger.debug("response from report url is {}".format(response))


        transaction = utils.convert_transaction_json_2_object(transaction)

    return render_template('transaction.html', form=form, transaction=transaction)

@bp.route('/client', methods=['GET', 'POST'])
def client():

    customer_info = None

    form = TransactionForm()
    if form.validate_on_submit():

        data = {"transactionId": form.transaction_id.data}

        current_app.logger.debug("filter data for transaction is {}".format(data))

        response = services.post_query(current_app.config['CLIENT_URL'], data)

        customer_info = response['customerInfo']

        if customer_info is None:
            current_app.logger.debug("no response_data found {}".format(customer_info))
            abort(404)

        current_app.logger.debug("response from report url is {}".format(response))

        customer_info = utils.convert_customer_json_2_object(customer_info)

    return render_template('client.html', form=form, customer=customer_info)