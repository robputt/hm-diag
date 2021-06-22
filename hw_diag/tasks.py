import logging
import json

# We use this for now to fake the diagnostics JSON
from hw_diag.tests.fixtures.diagnostic_results import SAMPLE_DIAGNOSTICS


log = logging.getLogger()
log.setLevel(logging.DEBUG)


def perform_hw_diagnostics():
    log.info('Running periodic hardware diagnostics')
    with open('diagnostic_data.json', 'w') as f:
        json.dump(SAMPLE_DIAGNOSTICS, f)
    log.info('Diagnostics complete')
