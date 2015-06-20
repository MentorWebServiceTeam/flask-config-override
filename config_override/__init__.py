from raven.contrib.flask import Sentry
import time
import os
import logging
import sys

def repeat_it(func, number, wait_message="Sleeping while calling function, try %s/%s"):
    """
    Assumes the function will throw needing retry if it errors, not throw if it succeeds.
    Will wait a second for `number` of seconds retrying each time, printing wait_message to stdout.
    Iterpolates the current attempt number and total number of tries.
    Finally it calls the method one more time if it has yet to succeed, this time the error will bubble
    """
    counter = 0
    for i in range(1, number + 1):
        try:
            func()
            return
        except Exception as e:
            time.sleep(1)
            print wait_message % (i, number)
    func()

def environment_override(app):
    for key in os.environ:
        if key in app.config:
            value = os.environ[key].strip()
            if len(value) == 0:
                continue
            try:
                value = int(value)
            except:
                pass
            if value == "True":
                value = True
            elif value == "False":
                value = False
            app.logger.info("Overridding %s from environment variable" % key)
            app.config[key] = value 

def basic_app_config(app, explicit_configs, config_list=["LOCAL_DEFAULT_CONFIG", "LOCAL_APP_CONFIG"], attempts=20):
    """
    Basic app config loads the config_list in order, waiting up to `attempts` seconds per file.
    Raises errors if the file is not found in that time.
    """
    for f in config_list:
        try:
            repeat_it(
                lambda: app.config.from_pyfile(os.environ[f], silent=False), 
                attempts,
                wait_message="Loading " + f + ". Try %s/%s"
            )
        except Exception as e:
            app.logger.info("Attempted to load default config environment var: %s but it failed. %s" % (f, e.message))
            raise

    environment_override(app)

    for key in explicit_configs:
        app.config[key] = explicit_configs[key]

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") 
    app.logger.handlers[0].setFormatter(formatter)
    if not app.debug:
        app.logger.addHandler(logging.StreamHandler(sys.stdout))
        app.logger.handlers[-1].setFormatter(formatter)
        app.logger.info("Not debug mode")
    else:
        app.logger.info("Debug mode")
    if 'SENTRY_DSN' in app.config:
        sentry = Sentry(app)
