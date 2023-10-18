class BasicConfig:
    USER_DB = "postgres"
    PASS_DB = "19100209"
    URL_DB = "localhost"
    NAME_BD = "flask_clase"
    FULL_URL_DB = f"postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_BD}"
    SQLALCHEMY_DATABASE_URI = FULL_URL_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "llave_secreta"
