import logging

from core.System import BaseController
from core.System.Entities.StockEntity import StockEntity
from core.models import Stock


class StockController(BaseController):
    def get_stock_obj(self):
        try:
            return StockEntity(Stock)
        except Exception as _e:
            logging.error(f"[StockController] Error 'get_stock_obj': {_e}")
