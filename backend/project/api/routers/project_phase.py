from ninja import Router
from project.api.views.project_phase import project_phase_router

router = Router()
router.add_router("/", project_phase_router)
