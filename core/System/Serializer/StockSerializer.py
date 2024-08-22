from core.System.BaseSerializer import BaseSerializer


class StockSerializer(BaseSerializer):
    fields = [
        'id',
        'name',
        'address',
    ]
