class AuthorRouter:
    author_db = "authors"   # sqlite db config's dict-key-name: "authors"
    default_db = "default"  # sqlite db config's dict-key-name: "default"

    def db_to_read(self, model, **hints):
        appLabel = model._meta.app_label
        if appLabel == "authorApp":
            return self.author_db
        return self.default_db

    def db_to_write(self, model, **hints):
        appLabel = model._meta.app_label
        if appLabel == "authorApp":
            return self.author_db
        return self.default_db
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Check what value the migrate/migrations cmd contains as "--database" flag; the value must be equal to one of the dict-key from the db-config-setting.
        # if model_name == "author":
        #     return db == "authors"
        # return db == "default"

        print("app_label (author_router):", app_label)
        print("model_name (author_router):", model_name)
        print("db (author_router):", db)
        # print("**hints (author_router):", hints)

        # if app_label == "authorApp":
        #     return db == self.author_db
        # return True
        # return db == self.default_db

        # # [WOKRING]
        # if model_name == "author":
        #     return db == self.author_db
        # return None
        # return db == self.default_db

        if db == 'authors':
            return app_label == 'authorApp' # allow migration for new django models implemented in legacy db
        elif app_label == 'authorApp':  # do not allow migration for legacy on any other db
            return False
        return None # this router not responsible
