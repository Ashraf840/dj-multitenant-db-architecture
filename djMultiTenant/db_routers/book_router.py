class Bookrouter:
    book_db = "books"   # sqlite db config's dict-key-name: "books"
    default_db = "default"  # sqlite db config's dict-key-name: "default"

    def db_for_read(self, model, **hints):
        # get lowercase-model-name from the model's meta information
        model_name = model._meta.model_name
        if model_name == "book":     # [Book -> book]
            return self.book_db
        return None

    def db_for_write(self, model, **hints):
        model_name = model._meta.model_name
        if model_name == "book":
            return self.book_db
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Check what value the migrate/migrations cmd contains as "--database" flag; the value must be equal to one of the dict-key from the db-config-setting.
        if model_name == "book":
            return db == "books"
        return db == "default"
