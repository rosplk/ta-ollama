TA-ollama (v0.1.1) — Ollama Monitoring for Splunk
by Rod Soto (rod@rodsoto.net)

==== OVERVIEW ====
This Technology Add-on enables Ollama monitoring in Splunk through:
• File monitoring of Ollama server logs
• HTTP Event Collector (HEC) for API telemetry and prompt data
• Built-in data parsing and field extraction
• CIM (Common Information Model) compliance for Web and Application State datamodels

==== INSTALLATION ====
1) Extract to Splunk apps directory:
   Windows: C:\Program Files\Splunk\etc\apps\TA-ollama-releasev1\
   Linux: /opt/splunk/etc/apps/TA-ollama-releasev1\
   
2) Restart Splunk

3) Verify: Check "TA-ollama" appears in Apps menu

==== CONFIGURATION ====

--- File Monitoring (Server Logs) ---
Method 1 - Splunk Web UI:
1) Settings > Data Inputs > Files & Directories > New
2) File/Directory: 
   Windows: C:\ProgramData\Ollama\logs\ollama.log
   Linux: ~/.ollama/logs/server.log
3) Sourcetype: ollama:server
4) Index: main (or preferred)
5) Save and enable

Method 2 - Configuration File:
1) Create local/inputs.conf in app directory:
   [monitor://C:\ProgramData\Ollama\logs\ollama.log]
   disabled = 0
   sourcetype = ollama:server
   index = main

2) Restart Splunk

--- HTTP Event Collector (API + Prompts) ---
1) Enable HEC: Settings > Data Inputs > HTTP Event Collector > Global Settings
2) Create HEC token: New Token > Allow all indexes
3) Configure your applications to send data to:
   https://your-splunk:8088/services/collector

==== DATA SOURCES ====

1) Server Logs (sourcetype=ollama:server)
   • Native Ollama log files
   • Error messages and debug info
   • Automatic data redaction (emails, API keys)

2) API Telemetry (sourcetype=ollama:api) - via HEC
   • Model information and usage stats
   • Example HEC payload:
   {
     "sourcetype": "ollama:api",
     "event": {
       "action": "tags",
       "host": "localhost",
       "models": ["llama3.1", "codellama"],
       "timestamp": "2024-01-01T10:00:00Z"
     }
   }

3) Prompt Data (sourcetype=ollama:prompts) - via HEC
   • Prompt and response tracking
   • Example HEC payload:
   {
     "sourcetype": "ollama:prompts", 
     "event": {
       "model": "llama3.1",
       "prompt": "What is AI?",
       "response": "Artificial Intelligence is...",
       "duration_ms": 1500,
       "timestamp": "2024-01-01T10:00:00Z"
     }
   }

==== TESTING ====

1) Test file monitoring:
   index=main sourcetype=ollama:server | head 5

2) Test HEC data (after configuring applications):
   index=main sourcetype=ollama:api | head 5
   index=main sourcetype=ollama:prompts | head 5

3) Summary view:
   index=main (sourcetype=ollama:*) | stats count by sourcetype

==== SAMPLE SEARCHES ====

Monitor server health:
index=main sourcetype=ollama:server "error" | timechart count

Track model usage (via HEC):
index=main sourcetype=ollama:prompts 
| stats count avg(duration_ms) by model

View recent prompts (redacted):
index=main sourcetype=ollama:prompts 
| table _time model prompt response

==== CIM-COMPLIANT SEARCHES ====

Web datamodel - HTTP requests:
| datamodel Web Web search | search app="ollama" 
| stats count by http_method, http_response_code

Application performance monitoring:
| datamodel Web Web search | search app="ollama"
| stats avg(response_time_ms) by uri_path | sort -avg(response_time_ms)

Security analysis - failed requests:
| datamodel Web Web search | search app="ollama" http_response_code>=400
| stats count by src, uri_path | sort -count

==== CIM DATAMODEL ACCELERATION ====
For optimal CIM performance, manually enable datamodel acceleration:
1. Go to Settings > Data Models
2. Find "Web" and "Application_State" datamodels  
3. Click "Edit" > "Accelerate" > Configure settings
4. Recommended: Enable with 7-day earliest time

==== NOTES ====
• All inputs disabled by default for security
• Sensitive data automatically redacted
• Compatible with Splunk Cloud Platform
• HEC configuration required for API/prompt data
• CIM 5.0+ compliance for Web and Application State datamodels
• Compatible with Splunk Enterprise Security and other CIM-dependent apps
• Datamodel acceleration NOT automatically enabled (manual setup required)