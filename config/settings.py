from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="PARSER",
    settings_files=["settings.toml", "settings.local.toml", ".secrets.toml", ".env"],
)