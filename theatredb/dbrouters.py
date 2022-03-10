class DbRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'theatre':
            return 'theatre_prod'
        else:
            return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'theatre':
            return 'theatre_prod'
        else:
            return None