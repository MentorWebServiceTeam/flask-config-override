import config_override
from flask import Flask
from nose.tools import assert_raises
import os

def test_without_environment():
    app = Flask(__name__)
    assert_raises(Exception, config_override.basic_app_config, app, {}, attempts=1)

def test_with_environment():
    app = Flask(__name__)
    os.environ['ITEM'] = "/file_thing_that_doesntexist"
    assert_raises(Exception, config_override.basic_app_config, app, {}, config_list=['ITEM'], attempts=2)
    del os.environ['ITEM']

def test_with_real_config():
    app = Flask(__name__)
    os.environ['ITEM'] = "test_config.py"
    config_override.basic_app_config(app, {}, config_list=['ITEM'])
    assert app.config['SOME_TEST_KEY'] == "MyTestString"

def test_with_sentry():
    app = Flask(__name__)
    os.environ['ITEM'] = "test_config.py"
    config_override.basic_app_config(app, {"SENTRY_DSN": "https://fe015ba0684b48b9a8b79cbcc4addddd:8b5a7d4353354d9eae63d579093c2561@app.getsentry.com/46208"}, config_list=['ITEM'])
    print app.extensions
    print app.config
    assert 'sentry' in app.extensions

def test_with_real_config_explicit_override():
    app = Flask(__name__)
    os.environ['ITEM'] = "test_config.py"
    os.environ['SOME_TEST_KEY'] = "ValueFromEnvironment"
    config_override.basic_app_config(app, {"SOME_TEST_KEY": "ExplicitValue"}, config_list=['ITEM'])
    assert app.config['SOME_TEST_KEY'] == "ExplicitValue"

def test_with_real_config_env_override():
    app = Flask(__name__)
    os.environ['ITEM'] = "test_config.py"
    os.environ['SOME_TEST_KEY'] = "ValueFromEnvironment"
    config_override.basic_app_config(app, {}, config_list=['ITEM'])
    assert app.config['SOME_TEST_KEY'] == "ValueFromEnvironment"

def test_with_real_config_env_override_empty():
    app = Flask(__name__)
    os.environ['ITEM'] = "test_config.py"
    os.environ['SOME_TEST_KEY'] = ""
    config_override.basic_app_config(app, {}, config_list=['ITEM'])
    assert app.config['SOME_TEST_KEY'] == "MyTestString"

def test_with_real_config_env_override_bool():
    app = Flask(__name__)
    os.environ['ITEM'] = "test_config.py"
    os.environ['SOME_TEST_KEY'] = "True"
    config_override.basic_app_config(app, {}, config_list=['ITEM'])
    assert app.config['SOME_TEST_KEY'] == True

def test_with_real_config_env_override_bool2():
    app = Flask(__name__)
    os.environ['ITEM'] = "test_config.py"
    os.environ['SOME_TEST_KEY'] = "False"
    config_override.basic_app_config(app, {}, config_list=['ITEM'])
    assert app.config['SOME_TEST_KEY'] == False