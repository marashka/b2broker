from django.db import models

from app.settings import MONEY_DECIMAL_PLACES, MONEY_MAX_DIGITS


class Wallet(models.Model):
    label = models.CharField(max_length=255, db_index=True)
    balance = models.DecimalField(
        max_digits=MONEY_MAX_DIGITS, decimal_places=MONEY_DECIMAL_PLACES, default=0
    )

    class Meta:
        ordering = ["id"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(balance__gte=0), name="wallet_balance_non_negative"
            ),
        ]


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT)
    txid = models.CharField(max_length=255, unique=True, blank=False)
    amount = models.DecimalField(
        max_digits=MONEY_MAX_DIGITS, decimal_places=MONEY_DECIMAL_PLACES
    )

    class Meta:
        ordering = ["id"]
