from fastapi import FastAPI

from app.routes import resume,ats,jobs, interview, dsa, auth


app=FastAPI(
    title="Prepo AI Career Assistant"
)



app.include_router(
    resume.router
)

app.include_router(
    ats.router
)

app.include_router(
    jobs.router
)

app.include_router(
    interview.router
)

app.include_router(
    dsa.router
)

app.include_router(
    auth.router
)

@app.get("/")
def home():

    return {
        "message":
        "Prepo Backend Running"
    }