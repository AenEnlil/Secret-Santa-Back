from fastapi import FastAPI


def get_application() -> FastAPI:
    application = FastAPI()

    @application.get("/")
    async def root():
        return {"message": "Hello World"}

    return application


app = get_application()
