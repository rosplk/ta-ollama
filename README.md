Splunk Technology Add-on for Ollama Large Language Model Monitoring

![492114d1-4209-4898-b101-85e7c0f3d98f](https://github.com/user-attachments/assets/5ba5ffa1-2781-4084-93a2-bc5127f0b37c)
![835f0cc3-18c2-4137-a1d0-3032c2489178](https://github.com/user-attachments/assets/513db398-c1a7-4da0-b80e-90cede73e6eb)
![3c96c015-66aa-4c9d-a9e2-96ecbb32e008](https://github.com/user-attachments/assets/4c2634c1-a728-43ae-b74f-e130641dca35)
![0da3cc15-c041-4a09-86a3-a1577a64d160](https://github.com/user-attachments/assets/04e5efc5-07b5-4687-af69-517e64e70bb6)

Overview

TA-ollama provides comprehensive monitoring capabilities for Ollama large language model deployments within Splunk. The add-on enables organizations to gain operational visibility into their LLM infrastructure through file monitoring, custom telemetry collection and enterprise-grade CIM compliance.

Features:

- File Monitoring: Automatic ingestion of Ollama server HTTP access logs
- HEC Integration: Flexible data collection via HTTP Event Collector
- CIM Compliance: Full Common Information Model support for enterprise security
- Security First: Built-in data redaction and secure defaults
- Cross-Platform: Windows and Linux Support
- Cloud Ready: Validated for Splunk Cloud Platform

Quick start

- Upload app to Splunk instance then configure data source input

Data Sources

- ollama:server (HTTP access logs withg GIN parsing) can be collected via file monitoring
- ollama:api (Custom API telemetry) Collected via HEC
- ollama:prompts (LLM Usage analytics) Collected via HEC

Supported Data Models
- Web
- Application_State

CIM Fields
- src, dest, http_response_code, http_method
- uri_path, response_time_ms, vendor_product, app
