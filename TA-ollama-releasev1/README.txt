Splunk Technology Add-on for Ollama Large Language Model Monitoring
by Rod Soto (rod@rodsoto.net)

Overview

TA-ollama provides comprehensive monitoring capabilities for Ollama large language model deployments within Splunk. The add-on enables organizations to gain operational visibility into their LLM infrastructure through file monitoring, custom telemetry collection and enterprise-grade CIM compliance.

Version 0.1.4 - CIM 5.0+ Compliance

Features:

- File Monitoring: Automatic ingestion of Ollama server HTTP access logs
- HEC Integration: Flexible data collection via HTTP Event Collector
- CIM 5.0+ Common Information Model Compliance support for Web datamodel
- Security First: Built-in data redaction and secure defaults
- Cross-Platform: Windows and Linux Support

Quick start

- Upload app to Splunk instance then configure data source input

Data Sources

- ollama:server (HTTP access logs with GIN parsing) can be collected via file monitoring
- ollama:api (Custom API telemetry) Collected via HEC
- ollama:prompts (LLM Usage analytics) Collected via HEC

Supported Data Models
- Web (CIM 5.0+ compliant)

CIM Web Fields (v0.1.4)
**Core Required Fields:**
- src, dest, action, status, url
- http_method, uri_path, http_response_code
- response_time_ms, duration

**Extended Fields:**
- bytes_in, bytes_out
- http_user_agent, http_referrer
- site, dest_port, src_port
- transport, protocol
- web_method, uri_query
- vendor_product, app, category, product

**Metadata Fields:**
- http_content_type

Installation

1. Download ta-ollama_014.tgz (https://splunkbase.splunk.com/app/8024)
2. Install via Splunk Web: Apps > Manage Apps > Install app from file > restart
3. Configure inputs via Settings > Data Inputs > Files & Directories

Testing CIM Compliance

Run these searches to verify CIM 5.0+ compliance:
```spl
| datamodel Web search
  | search Web.vendor_product="Ollama API Server"
  | rename Web.* as *
  | stats count by _time src dest url http_method status http_content_type

index=main sourcetype=ollama:server
| stats count by action, src, dest, http_method, status, url, protocol
```

Release Notes v0.1.4

Fixes:
- Fixed AWS Splunk compatibility issue with `ollama_static_cim_fields` transform validation error
- Migrated static CIM field assignments from transforms.conf to EVAL statements in props.conf for better cross-platform compatibility

Requirements

- Splunk Enterprise 8.0+ or Splunk Cloud Platform
- Ollama server running with GIN logging format
- For HEC inputs: HTTP Event Collector configured

License

MIT License - See LICENSE file for details

Support

- Author: Rod Soto (rod@rodsoto.net)
- Issues: Report via GitHub issues
- Documentation: See README folder for detailed guides