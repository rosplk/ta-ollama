# CHANGELOG

## Version 0.1.3 (2025-10-10)

### CIM 5.0+ Compliance Enhancements
- **Web Datamodel Compliance**: Improved CIM 5.0+ Web datamodel fields
  - Added `bytes_in` and `bytes_out` fields (set to 0 for API logs)
  - Added `http_user_agent` with default "Ollama-Client"
  - Added `http_referrer`, `site`, `dest_port`, `transport`, `protocol`
  - Added `web_method`, `uri_query`, `http_content_type`
  - Enhanced `action` field to "allowed" for better CIM compliance

### Field Extraction Improvements
- Improved IPv6 support in regex patterns (handles ::ffff: prefix)
- Enhanced static field mappings with `product` field
- Added `vendor_action` for action field aliasing
- Better null handling for optional fields

### Tags Enhancement
- Added `communicate` tag to ollama_server eventtype for better categorization

### Documentation
- Updated version to 0.1.3 in app.conf
- Enhanced description to reflect full CIM 5.0+ compliance

## Version 0.1.2
- Initial CIM Web datamodel support
- Basic field extractions for GIN logs
- Security redactions for emails and API keys

## Version 0.1.1
- Initial release
- File monitoring support
- HEC integration
- Basic Ollama log parsing
