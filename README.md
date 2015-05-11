# flask-config-override
Flask app configuration methods, with environment overrides and waiting (for docker config providers w/ race conditions)

Bring this basic configuration module into your app for overridable configuration.

The api is

```config_override.basic_app_config(app, dict_of_explicit_overrides, list_of_env_vars)```

Where ```app``` is the flask app, and ```list_of_env_vars``` is a list of environment variable names that contain file paths.

