from ninja import Router
from material.api.views.wood_species import wood_species_router

router = Router()
router.add_router("/", wood_species_router)
