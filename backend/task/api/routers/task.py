from ninja import Router
from task.api.views.task import task_router

router = Router()
router.add_router("/", task_router)
