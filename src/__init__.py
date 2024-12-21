from fastapi import FastAPI, Depends
from src.dependencies import validate_schoolname_header
from src.auth.routes import auth_router
from src.admission.routes import admission_router
from src.faculty.routes import faculty_router
from src.school.routes import school_router
from src.timetable.routes import timetable_router
from src.events.routes import events_router
from src.leave.routes import leave_router
from src.homework.routes import homework_router
from src.complaint.routes import complaint_router
from src.feedback.routes import feedback_router

version = "v1"

description = """
    Backend oriented for the school project.
"""

version_prefix = f"/api/{version}"

app = FastAPI(
    title="schoolBackend",
    description=description,
    version=version,
    license_info={"name": "MIT License", "url": "https://opensource.org/license/mit"},
    contact={
        "name": "Bayya Mohith",
        "url": "https://github.com/Mohith705",
        "email": "bayyamohith32@gmail.com",
    },
    terms_of_service="httpS://example.com/tos",
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc",
    dependencies=[Depends(validate_schoolname_header)]
)

app.include_router(auth_router, prefix=f"{version_prefix}/auth", tags=["auth"])
app.include_router(admission_router, prefix=f"{version_prefix}/admission", tags=["admission"])
app.include_router(faculty_router, prefix=f"{version_prefix}/faculty", tags=["faculty"])
app.include_router(school_router, prefix=f"{version_prefix}/school", tags=["school"])
app.include_router(timetable_router, prefix=f"{version_prefix}/timetable", tags=["timetable"])
app.include_router(events_router, prefix=f"{version_prefix}/events", tags=["events"])
app.include_router(leave_router, prefix=f"{version_prefix}/leave", tags=["leave"])
app.include_router(homework_router, prefix=f"{version_prefix}/homework", tags=["homework"])
app.include_router(complaint_router, prefix=f"{version_prefix}/complaint", tags=["complaint"])
app.include_router(feedback_router, prefix=f"{version_prefix}/feedback", tags=["feedback"])