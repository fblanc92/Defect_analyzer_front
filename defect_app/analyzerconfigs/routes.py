from flask_login import current_user, login_required
from flask import render_template, request, Blueprint, flash, redirect, url_for, abort
from Defect_analyzer_front.defect_app import db
from Defect_analyzer_front.defect_app.models import Analyzer_config
from Defect_analyzer_front.defect_app.analyzerconfigs.forms import AnalyzerConfigForm
from Defect_analyzer_back.resources.config.configs_utils import get_all_the_configs_list
analyzer_config_blueprint = Blueprint('analyzer_config_blueprint', __name__)


@analyzer_config_blueprint.route('/analyzer_config')
@login_required
def analyzer_config():  # Home | About | Analyzer Configs
    page = request.args.get('page', 1, type=int)
    configs = Analyzer_config.query.order_by(Analyzer_config.date_created.desc()).paginate(page=page, per_page=5)
    return render_template('analyzer_config_bak.html', configs=configs)


@analyzer_config_blueprint.route('/analyzer_config/new', methods=['GET', 'POST'])
@login_required
def edit_config():  # no argument config_id argument because the idea is edit the ONLY config
    form = AnalyzerConfigForm()
    if form.validate_on_submit():  # se crea una nueva, no se edita la actual para tener historia

        new_config = Analyzer_config(title=form.title.data,
                                     author=current_user,
                                     description=form.description.data,
                                     model_path=form.model_path.data,
                                     labels_path=form.labels_path.data,
                                     input_images_path=form.input_images_path.data,
                                     output_images_path=form.output_images_path.data,
                                     image_saving=form.image_saving.data,
                                     generate_template=form.generate_template.data)
        db.session.add(new_config)
        db.session.commit()
        flash('The configuration has been updated', 'success')
        return redirect(url_for('analyzer_config_blueprint.edit_config'))

    def create_default_config():
        return Analyzer_config(title=' ',
                               author=current_user,
                               description=' ',
                               model_path=' ',
                               labels_path=' ',
                               input_images_path=' ',
                               output_images_path=' ',
                               image_saving=False,
                               generate_template=True)

    if not Analyzer_config.query.all():
        current_config = create_default_config()
    else:
        current_config = Analyzer_config.query.order_by(Analyzer_config.date_created.desc()).first()

    form.title.data = current_config.title
    form.description.data = current_config.description
    form.model_path.data = current_config.model_path
    form.labels_path.data = current_config.labels_path
    form.input_images_path.data = current_config.input_images_path
    form.output_images_path.data = current_config.output_images_path
    form.image_saving.data = current_config.image_saving
    form.generate_template.data = current_config.generate_template

    return render_template('edit_config_bak.html', title='Edit Config', form=form, legend='Edit Config')
