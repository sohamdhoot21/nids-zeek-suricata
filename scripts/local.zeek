@load base/frameworks/input
@load base/frameworks/notice
@load base/frameworks/sumstats
@load base/protocols/conn
@load base/protocols/dns
@load base/protocols/http
@load base/protocols/ssh
@load base/protocols/ssl

# Configure the network interface
redef interface = "en0";

# Configure logging
redef LogAscii::logdir = "/opt/zeek/logs";
redef LogAscii::use_json = T;
redef LogAscii::json_timestamps = JSON::TS_ISO8601;

# Remove Elasticsearch direct output as we'll use Logstash instead
# Ensure rotation is configured correctly for Logstash pickup
redef Log::default_rotation_interval = 3600sec;
redef Log::default_rotation_postprocessor_cmd = "";

# Define local networks
redef Site::local_nets = { 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12 };

# Load additional protocol analyzers for better visibility
@load protocols/ftp
@load protocols/smtp
@load protocols/sip
@load protocols/snmp
@load protocols/syslog
@load protocols/modbus
@load protocols/rdp
@load protocols/mysql

# File analysis capabilities
@load frameworks/files/hash-all-files
@load frameworks/files/detect-MHR

# Enable Intel framework for threat intelligence
@load frameworks/intel/seen
@load frameworks/intel/do_notice

# Enable detecting various attacks
@load misc/detect-traceroute
@load misc/scan
@load misc/weird
@load-sigs frameworks/signatures/detect-windows-shells 