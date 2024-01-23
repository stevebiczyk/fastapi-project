from fastapi import FastAPI

app = FastAPI(
    docs_url="/documentation",
    redoc_url="/redocs",
    title="Real Estate Services",
    description="This is a simlpe real estate listings API.",
    version="1.0.0",
    contact={
        name:"Istvan",
        website:"https://istvanbiczyk.com",
        email:"istvan@istvanbiczyk.com"
    }
)
