from rest_framework import mixins, viewsets

from wallets.models import Transaction, Wallet
from wallets.serializers import TransactionSerializer, WalletSerializer


class WalletViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    filterset_fields = {
        "label": ("icontains", "iexact", "contains"),
        "balance": ("exact", "lt", "lte", "gt", "gte"),
    }
    ordering = ["label"]
    ordering_fields = ["label", "balance"]


class TransactionViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    filterset_fields = {
        "txid": ("exact",),
        "amount": ("exact", "lt", "lte", "gt", "gte"),
        "wallet__id": ("exact",),
    }
    ordering = ["txid"]
    ordering_fields = ["txid", "amount"]
