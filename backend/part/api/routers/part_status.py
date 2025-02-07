from ninja import Router
from part.api.views.part_status import part_status_router

router = Router()
router.add_router("/", part_status_router)
