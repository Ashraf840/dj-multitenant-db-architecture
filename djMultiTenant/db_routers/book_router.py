class BookRouter:
    book_db = "books"   # sqlite db config's dict-key-name: "books"
    default_db = "default"  # sqlite db config's dict-key-name: "default"

    def db_to_read(self, model, **hints):
        appLabel = model._meta.app_label
        if appLabel == "booksApp":
            return self.book_db
        return self.default_db

    def db_to_write(self, model, **hints):
        appLabel = model._meta.app_label
        if appLabel == "booksApp":
            return self.book_db
        return self.default_db
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Check what value the migrate/migrations cmd contains as "--database" flag; the value must be equal to one of the dict-key from the db-config-setting.
        # if model_name == "book":
        #     return db == "books"
        # return db == "default"

        print("app_label (book_router):", app_label)
        # print("model_name (book_router):", model_name)
        print("db (author_router):", db)
        # print("**hints (book_router):", hints)

        # if app_label == "booksApp":
        #     return db == self.book_db
        # return True
        # return db == self.default_db

        # # [WOKRING]
        # if model_name == "book":
        #     return db == self.book_db
        # return None
        # return db == self.default_db

        if db == 'books':
            return app_label == 'booksApp' # allow migration for new django models implemented in legacy db
        elif app_label == 'booksApp':  # do not allow migration for legacy on any other db
            return False
        return None # this router not responsible