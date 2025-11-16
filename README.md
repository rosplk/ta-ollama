Splunk Technology Add-on for Ollama Large Language Model Monitoring
by Rod Soto 
<img width="1272" height="442" alt="cimv51" src="https://github.com/user-attachments/assets/c8d98c64-9825-4eeb-bbb6-0c21ae663a60" />
<img width="1268" height="626" alt="cimv52" src="https://github.com/user-attachments/assets/385c2ce7-c813-4f39-bd3c-db4a89f09443" />




Overview

TA-ollama provides comprehensive monitoring capabilities for Ollama large language model deployments within Splunk. The add-on enables organizations to gain operational visibility into their LLM infrastructure through file monitoring, custom telemetry collection and CIM compliance.

Version 0.1.3 - CIM 5.0+ Compliance

Features:

- File Monitoring: Automatic ingestion of Ollama server HTTP access logs
- HEC Integration: Flexible data collection via HTTP Event Collector
- CIM 5.0+ Compliance: Common Information Model support for Web datamodel
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

CIM Web Fields (v0.1.3)
**Core Required Fields:**
- src, dest, action, status, url
- http_method, uri_path, http_response_code
- response_time_ms, duration

**Extended Fields:**
- bytes_in, bytes_out
- http_user_agent
- site, dest_port
- transport, protocol
- web_method, uri_path
- app

**Metadata Fields:**
- http_content_type

Installation

1. Download TA-ollama-v0.1.3.tgz
2. Install via Splunk Web: Apps > Manage Apps > Install app from file
3. Configure inputs via Settings > Data Inputs > Files & Directories

Testing CIM Compliance

Run these searches to verify CIM 5.0+ compliance:

```spl
| datamodel Web search
  | search Web.vendor_product="Ollama API Server"
  | rename Web.* as *
  | stats count by _time src dest url http_method status http_content_type

index=main sourcetype=ollama:server
| stats count by src, dest, http_method, status, url, protocol

```
Linux Server Logging Setup

<img width="1743" height="856" alt="Screenshot from 2025-11-15 20-45-05" src="https://github.com/user-attachments/assets/e02883c1-2340-44ce-a5a0-b46706fdde03" />


  Important: Ollama on Linux logs to systemd/journalctl by default, not to files. You must configure file-based logging for
   the TA to collect data.

  Quick Setup

  1. Create log directory:
  sudo mkdir -p /var/log/ollama
  sudo chown ollama:ollama /var/log/ollama
  sudo chmod 755 /var/log/ollama

  2. Configure systemd service:

  Edit /etc/systemd/system/ollama.service and add these lines in the [Service] section:

  StandardOutput=append:/var/log/ollama/ollama.log
  StandardError=append:/var/log/ollama/ollama.log

  Complete example:
  [Unit]
  Description=Ollama Service
  After=network-online.target

  [Service]
  ExecStart=/usr/local/bin/ollama serve
  User=ollama
  Group=ollama
  Restart=always
  RestartSec=3
  Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

  # Log configuration - redirect stdout and stderr to log file
  StandardOutput=append:/var/log/ollama/ollama.log
  StandardError=append:/var/log/ollama/ollama.log

  [Install]
  WantedBy=default.target

  Log Verbosity Levels

  Control log verbosity with the OLLAMA_DEBUG environment variable. Add this to the [Service] section:

  INFO (Recommended for Production):
  Environment="OLLAMA_DEBUG=INFO"
  - Includes HTTP access logs (GIN format) required for Splunk CIM compliance
  - Server startup/shutdown events
  - Model loading notifications
  - Moderate log volume

  DEBUG (Verbose - for troubleshooting):
  Environment="OLLAMA_DEBUG=DEBUG"
  - All INFO logs plus detailed internal debugging
  - Higher log volume - consider log rotation
  - Useful for troubleshooting issues

  WARN (Minimal logging):
  Environment="OLLAMA_DEBUG=WARN"
  - Only warnings and errors
  - May miss some HTTP access logs
  - Not recommended for Splunk monitoring

  Default: If not specified, Ollama defaults to INFO level.

  3. Apply changes:
  sudo systemctl daemon-reload
  sudo systemctl restart ollama

  4. Verify logging:
  sudo tail -f /var/log/ollama/ollama.log

  You should see GIN-formatted HTTP access logs like:
  [GIN] 2025/11/15 - 20:24:51 | 200 | 47.014µs | 127.0.0.1 | POST "/api/generate"

  5. Configure log rotation (recommended):

  Create /etc/logrotate.d/ollama:
  /var/log/ollama/ollama.log {
      daily
      rotate 7
      compress
      delaycompress
      missingok
      notifempty
      create 0644 ollama ollama
  }

  6. Configure Splunk input:

  In Splunk, add to local/inputs.conf:
  [monitor:///var/log/ollama/ollama.log]
  disabled = 0
  index = main
  sourcetype = ollama:server

  Note: Windows and macOS users can skip this section - Ollama creates log files automatically on those platforms.

Requirements

- Splunk Enterprise 8.0+ or Splunk Cloud Platform
- Ollama server running with GIN logging format
- For HEC inputs: HTTP Event Collector configured


License

MIT License - See LICENSE file for details

Support

- Author: Rod Soto (rod@rodsoto.net)
- Issues: Report via GitHub issues


