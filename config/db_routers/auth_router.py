from django.contrib.sessions.models import Session


class AuthRouter:
    route_app_labels = {"users", "auth", "contenttypes", "sessions", "admin", "messages"}
    users_db = "users_db"

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.users_db
        return None

    def db_for_write(self, model, **hints):
        if model is Session:
            return self.users_db
        if model._meta.app_label in self.route_app_labels:
            return self.users_db
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Make sure the auth and contenttypes apps only appear in the
        'users_db' database."""
        if app_label in self.route_app_labels:
            return db == self.users_db
        return None
