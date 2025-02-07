from ninja import Router
from project.api.views.project import project_router

router = Router()
router.add_router("/", project_router)
