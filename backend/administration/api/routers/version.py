from ninja import Router
from administration.api.views.version import version_router

router = Router()
router.add_router("/", version_router)
