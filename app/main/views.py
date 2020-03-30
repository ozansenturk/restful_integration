from app.main import bp
from flask import render_template,request, url_for,current_app,flash, redirect
from app.main.forms import ReportForm
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

        email = current_app.config['EMAIL']
        password = current_app.config['PASSWORD']
        token = services.get_token(current_app.config['LOGIN_URL'], email, password)

        current_app.logger.debug("token is {}".format(token))

        one_token = token['token']
        status = token['status']

        if status != 'APPROVED':
            current_app.logger.debug("status is {}".format(status))
            abort(500)


        data = {"fromDate": form.fromDate.data.strftime('%Y-%m-%d'), "toDate": form.toDate.data.strftime('%Y-%m-%d')}

        data = utils.add_to_dict_if_form_field_exist(data, 'acquirer', form.acquirer.data, True)
        data = utils.add_to_dict_if_form_field_exist(data, 'merchant', form.merchant.data, True)

        current_app.logger.debug("filter data for report is {}".format(data))

        response = services.post_query(current_app.config['REPORT_URL'], one_token, data)

        response_status = response['status']
        response_list = response['response']

        if status != 'APPROVED':
            current_app.logger.debug("response_status is {}".format(response_status))
            abort(500)
        elif len(response_list) == 0:
            current_app.logger.debug("no response_data found {}".format(response_list))
            abort(404)

        current_app.logger.debug("response from report url is {}".format(response))

        report_list = utils.convert_report_json_2_object(response_list)

    return render_template('report.html', form=form, reports=report_list)




