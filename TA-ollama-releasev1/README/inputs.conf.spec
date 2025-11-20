# TA-ollama inputs.conf.spec
# inputs.conf.spec for TA-ollama

[monitor://<path_to_ollama_logs>]
* Monitor Ollama server log files for ingestion into Splunk
* This stanza configures file monitoring for Ollama HTTP access logs
* Common paths:
*   Windows: C:\ProgramData\Ollama\logs\ollama.log
*   Linux: ~/.ollama/logs/server.log or /var/log/ollama/ollama.log

sourcetype = <string>
* Specifies the sourcetype to apply to events from this input
* Recommended: ollama:server
* Optional
* Default: ollama:server

index = <string>
* Specifies the index where events will be stored
* Optional
* Default: main

disabled = <boolean>
* Toggles whether this input is enabled
* Optional  
* Default: false

# HTTP Event Collector (HEC) Sourcetypes
# 
# This TA defines additional sourcetypes for use with HTTP Event Collector:
#
# ollama:api
#   * For API telemetry data sent via HEC
#   * Example fields: model, action, host, timestamp
#
# ollama:prompts
#   * For prompt and response data sent via HEC  
#   * Example fields: model, prompt, response, duration_ms
#
# HEC inputs do not require configuration in inputs.conf
# Configure HEC tokens in Splunk Web under Settings > Data Inputs > HTTP Event Collector