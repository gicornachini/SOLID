class Customer(object):

    def __init__(self, name):
        self.name = name

    def store_customer(self, name):
        """ Store into db responsibility. """
        pass

    def generate_customer_report(self, name):
        """ Generate report responsibility. """
        pass
