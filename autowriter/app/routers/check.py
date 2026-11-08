from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["check"])

NOT_IMPLEMENTED_MESSAGE = "Проверка текста пока не реализована."


@router.post("/check")
async def check_text() -> dict[str, str]:
    """Заглушка. Текст не читается и никуда не отправляется."""
    return {
        "status": "not_implemented",
        "message": NOT_IMPLEMENTED_MESSAGE,
    }
