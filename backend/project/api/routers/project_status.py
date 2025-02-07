from ninja import Router
from project.api.views.project_status import project_status_router

router = Router()
router.add_router("/", project_status_router)
