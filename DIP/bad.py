class DeliveryDriver(object):

    def deliver_product(self, product):
        # Deliver product...
        pass


class DeliveryCompany(object):

    def send_product(self, product):
        delivery_driver = DeliveryDriver()
        delivery_driver.deliver_product(product)
