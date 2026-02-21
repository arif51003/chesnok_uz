from .register import router as register_router
from .basic import router as basic_auth
from .session import router as session_auth
from .gwt import router as jwt_router

from fastapi import APIRouter

router=APIRouter(
    prefix="/auth",
    tags=["Authentication"]
    )

router.include_router(register_router)
router.include_router(basic_auth)
router.include_router(session_auth)
router.include_router(jwt_router)