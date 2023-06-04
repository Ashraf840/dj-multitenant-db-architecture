class AuthorRouter:
    author_db = "authors"   # sqlite db config's dict-key-name: "authors"
    default_db = "default"  # sqlite db config's dict-key-name: "default"

    def db_to_read(self, model, **hints):
        model_name = model._meta.model_name
        if model_name == "author":
            return self.author_db
        return self.default_db

    def db_to_write(self, model, **hints):
        model_name = model._meta.model_name
        if model_name == "author":
            return self.author_db
        return self.default_db
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Check what value the migrate/migrations cmd contains as "--database" flag; the value must be equal to one of the dict-key from the db-config-setting.
        if model_name == "author":
            return db == "authors"
        return db == "default"

        # if app_label == "author_label":
        #     return db == "authors"
        # return db == "default"
