from ninja import Router
from material.api.views.material_object import material_object_router

router = Router()
router.add_router("/", material_object_router)
