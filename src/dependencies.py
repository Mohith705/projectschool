# src/dependencies.py
from fastapi import Header, HTTPException, status

async def validate_schoolname_header(
    schoolname: str = Header(
        None,
        title="School Name",
        description="The name of the school for which the database is being queried.",
        example="school123"
    )
):
    if not schoolname:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The 'schoolname' header is required."
        )
    return schoolname
