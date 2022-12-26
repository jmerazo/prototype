from src.models.utils import DeliveryModel

deliveryModel = DeliveryModel()

class DeliveryController():
    def listDelivery(self):
        return deliveryModel.listDelivery()