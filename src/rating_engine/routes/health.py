from fastapi import APIRouter, HTTPException


# initalize the router
router= APIRouter()

@router.get("/health")
def health_check():
    """
        This function is used to check if the service is up.
    """
    try:
        return {"status": "Ok"}

    except Exception as e:
        raise HTTPException(detail=str(e))