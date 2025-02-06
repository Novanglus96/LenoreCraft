from ninja import Router
from material.api.views.material_status import material_status_router

router = Router()
router.add_router("/", material_status_router)
