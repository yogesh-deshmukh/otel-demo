from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from fastapi import FastAPI
import os

resource = Resource(attributes={
    "service.name": "FastAPI",
    "telemetry.sdk.language": "Python"
})

# Configure OTLP exporter to send traces to your collector endpoint
otlp_exporter = OTLPSpanExporter(
    endpoint= 'http://otel-collector:4317',
    # endpoint=os.environ.get("OTLP_ENDPOINT", "http://otel-collector:4318"),
    insecure=True
)

trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)

# Use the OTLP exporter with BatchSpanProcessor
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

app = FastAPI()

# Instrument your FastAPI application
FastAPIInstrumentor().instrument_app(app)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
