from rest_framework import routers

from wallets.views import TransactionViewSet, WalletViewSet

router = routers.DefaultRouter()
router.register(r"wallet", WalletViewSet)
router.register(r"transaction", TransactionViewSet)
