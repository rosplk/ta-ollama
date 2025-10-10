# TA-ollama inputs.conf.spec
# File monitoring and HEC configuration guide

# File Monitoring for Ollama Server Logs
[monitor://<path_to_ollama_logs>]
* Monitor Ollama server log files
* Common paths:
*   Windows: C:\ProgramData\Ollama\logs\ollama.log
*   Linux: ~/.ollama/logs/server.log or /var/log/ollama/ollama.log

sourcetype = ollama:server
* Use ollama:server sourcetype for proper parsing

index = <string>
* Target index (default: main)

disabled = <true|false>
* Enable/disable monitoring (default: true)

# HTTP Event Collector (HEC) Data Sources:
# 
# 1) API Telemetry (sourcetype=ollama:api)
#    Configure your monitoring tools to send Ollama API data via HEC
#    Example fields: model, action, host, timestamp
#
# 2) Prompt Data (sourcetype=ollama:prompts) 
#    Configure applications to send prompt/response data via HEC
#    Example fields: model, prompt, response, duration_ms
#
# No input configuration required for HEC - data sent directly to HEC endpoint

# CIM Compliance:
# This TA provides CIM 5.0+ compliance for:
# - Web datamodel (ollama:server HTTP access logs)
# - Application_State datamodel (service monitoring)
# 
# CIM Fields Available:
# src, dest, http_response_code, http_method, uri_path, response_time_ms, 
# vendor_product, app