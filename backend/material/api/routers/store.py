from ninja import Router
from material.api.views.store import store_router

router = Router()
router.add_router("/", store_router)
