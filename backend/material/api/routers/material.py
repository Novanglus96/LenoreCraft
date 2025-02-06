from ninja import Router
from material.api.views.material import material_router

router = Router()
router.add_router("/", material_router)
