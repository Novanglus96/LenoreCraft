from ninja import Router
from note.api.views.note import note_router

router = Router()
router.add_router("/", note_router)
