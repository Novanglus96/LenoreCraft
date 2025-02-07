from ninja import Router
from task.api.views.task_status import task_status_router

router = Router()
router.add_router("/", task_status_router)
