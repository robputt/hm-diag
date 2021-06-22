import logging

from flask import Flask
from flask_apscheduler import APScheduler

from hw_diag.tasks import perform_hw_diagnostics
from hw_diag.views.diagnostics import DIAGNOSTICS


log = logging.getLogger()
log.setLevel(logging.DEBUG)


def get_app(name):
    app = Flask(name)

    # Configure the backend scheduled tasks
    scheduler = APScheduler()
    scheduler.api_enabled = True
    scheduler.init_app(app)
    scheduler.start()

    # According to the original code we run the diagnostics
    # every 2 minutes, the frequency can be adjusted here...
    # TODO: Probably need to split this out into some conf file
    @scheduler.task('cron', id='run_diagnostics', minute='*/2')
    def run_diagnostics_task():
        perform_hw_diagnostics()

    # Register Blueprints
    app.register_blueprint(DIAGNOSTICS)

    return app


if __name__ == '__main__':
    app = get_app(__name__)
    app.run(threaded=True, debug=True)
