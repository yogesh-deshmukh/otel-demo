# OpenTelemetry Collector Demo Project

This project demonstrates the use of OpenTelemetry (OTel) Collector for collecting self-metrics and span metrics. The setup uses Docker Compose to run a Python FastAPI backend that generates traces, Prometheus to capture metrics, Jaeger to visualize traces, and Grafana to visualize collected metrics.

## Project Structure

- **otel-collector**: OTel Collector service configured to receive, process, and export telemetry data.
- **prometheus**: Service to scrape metrics from the OTel Collector and other services.
- **grafana**: Service to visualize the metrics collected by Prometheus.
- **jaeger**: Service to visualize the traces generated by the Python FastAPI backend.
- **my-python-api**: Python FastAPI backend to generate traces.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yogesh-deshmukh/otel-demo.git
    cd otel-demo
    ```

2. **Build and run the services**:
    ```bash
    docker-compose up --build
    ```

3. **Access the services**:
    - **Grafana**: [http://localhost:3000](http://localhost:3000)
    - **Prometheus**: [http://localhost:9090](http://localhost:9090)
    - **Jaeger**: [http://localhost:16686](http://localhost:16686)
    - **Python FastAPI**: [http://localhost:8091](http://localhost:8091)
    - **OTel Collector Prometheus Endpoint**: [http://localhost:8889/metrics](http://localhost:8889/metrics)

## Configuration Details

### OTel Collector

The OTel Collector is configured using the `otel-collector-config.yaml` file. This file includes configurations for receiving data via OTLP, processing the data, and exporting it to Prometheus and Jaeger.

### Prometheus

The Prometheus service uses `prometheus.yaml` for its configuration. This file includes scrape configurations for the OTel Collector and other relevant endpoints.

### Grafana

Grafana is configured with a custom `grafana.ini` file and provisioning files located in the `grafana/provisioning/` directory. These files setup data sources (Prometheus) and dashboards.

## Generating Traces and Metrics

The Python FastAPI backend (`my-python-api`) generates traces that are sent to the OTel Collector. The OTel Collector processes these traces and exports them to Jaeger for visualization. Metrics are collected by Prometheus and visualized using Grafana.

## Visualizing Metrics and Traces

- **Traces**: Visit [Jaeger UI](http://localhost:16686) to visualize traces.
- **Metrics**: Use [Grafana](http://localhost:3000) to create dashboards and visualize metrics collected by Prometheus.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
