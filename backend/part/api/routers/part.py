from ninja import Router
from part.api.views.part import part_router

router = Router()
router.add_router("/", part_router)
