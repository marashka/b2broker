from django.db import transaction
from django.db.models import F
from rest_framework_json_api import serializers

from wallets.models import Transaction, Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"
        read_only_fields = ["balance"]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

    def validate(self, data):
        wallet = data["wallet"]
        amount = data["amount"]
        if wallet.balance + amount < 0:
            raise serializers.ValidationError("wallet_balance_non_negative")
        return data

    def create(self, validated_data):
        wallet = validated_data["wallet"]
        amount = validated_data["amount"]

        with transaction.atomic():
            updated = Wallet.objects.filter(id=wallet.id, balance__gte=-amount).update(
                balance=F("balance") + amount
            )

            if not updated:
                raise serializers.ValidationError("insufficient wallet balance")

            return super().create(validated_data)
