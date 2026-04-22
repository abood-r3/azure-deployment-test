class AppDatabaseRouter:
    APP_DB_MAP = {
        # Django core / auth stack
        "auth": "ms0_db",
        "contenttypes": "ms0_db",
        "admin": "ms0_db",
        "sessions": "ms0_db",
        "sites": "ms0_db",
        # app specific tables, and the DB they are supposed to go to
        "ms0_usersAndAuth": "ms0_db",
        # "ms1_.....": "ms1_db",
        # "ms2_.....": "ms2_db",
    }

    def db_for_read(self, model, **hints):
        return self.APP_DB_MAP.get(model._meta.app_label)

    def db_for_write(self, model, **hints):
        return self.APP_DB_MAP.get(model._meta.app_label)

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations ONLY within same DB
        db1 = self.APP_DB_MAP.get(obj1._meta.app_label)
        db2 = self.APP_DB_MAP.get(obj2._meta.app_label)
        if db1 and db2:
            return db1 == db2
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        target_db = self.APP_DB_MAP.get(app_label)
        return db == target_db
