from django.urls import include, path

from wallets.urls import router as wallet_router

urlpatterns = [
    path("api/wallets/", include(wallet_router.urls)),
]
