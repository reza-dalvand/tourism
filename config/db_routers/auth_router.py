from apps.users.models import User

user_db = "users_db"


class AuthRouter:
    def db_for_read(self, model, **hints):
        if model is User:
            return user_db
        return None

    def db_for_write(self, model, **hints):
        if model is User:
            return user_db
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "users":
            return db == user_db

    # Use the default way for relation among instances
    # def allow_relation(self, obj1, obj2, **hints):
    #      pass
