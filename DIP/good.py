from abc import ABCMeta, abstractmethod


class DeliveryService(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def deliver_product(self, product):
        pass


class DeliveryDriver(DeliveryService):

    def deliver_product(self, product):
        # Implement deliver
        pass


class DeliveryCompany(object):

    def __init__(self, delivery_service):
        self.delivery_service = delivery_service

    def send_product(self, product):
        self.delivery_service.deliver_product(product)
