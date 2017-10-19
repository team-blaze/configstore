import configstore

configstore.enabled_backends = [
    configstore.DockerSecretBackend(),
    configstore.EnvVarBackend()
]

SECRET_KEY = configstore.get_config('APP_SECRET_KEY')
