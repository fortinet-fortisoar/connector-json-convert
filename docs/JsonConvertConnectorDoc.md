## About the connector
Convert the output of many commands and file-types to structured objects using the open-source JSON Convert (JC) library. The JC project details can be found at https://github.com/kellyjonbrazil/jc
<p>This document provides information about the JC - Parse Command Output Connector, which facilitates automated interactions, with a JC - Parse Command Output server using FortiSOAR&trade; playbooks. Add the JC - Parse Command Output Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with JC - Parse Command Output.</p>

### Version information

Connector Version: 1.0.0


Authored By: Community

Certified: No

## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-json-convert`

## Prerequisites to configuring the connector
There are no prerequisites to configuring this connector.

### Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
None.
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Convert<br></td><td>Convert command or file output to a Dict or List of Dicts.<br></td><td> <br/>Utilities<br></td></tr>
</tbody></table>

### operation: Convert
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>JC Parser<br></td><td>Select the correct parser to be used to convert the command or file output. Documentation for parsers can be found at https://github.com/kellyjonbrazil/jc#parsers. (This parameter will make an API call named "get_parser_list" to dynamically populate its dropdown selections)<br>
</td></tr><tr><td>Command or File Output to Parse<br></td><td>Enter the text string of the command or file output to be converted to a Dict or List of Dicts.<br>
</td></tr><tr><td>Raw Output<br></td><td>An unprocessed conversion that will typically not include int, float, or bool conversions. Also will not include additional calculated fields in the output. (e.g. timestamps)<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "api_data": ""
</code><code><br>}</code>


## Included playbooks
The `Sample - json-convert - 1.0.0` playbook collection comes bundled with the JC - Parse Command Output connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the JC - Parse Command Output connector.

- JC Convert Command Output: arp
- JC Convert Command Output: cat hosts
- JC Convert Command Output: date
- JC Convert Command Output: env
- JC Convert Command Output: file
- JC Convert Command Output: free
- JC Convert Command Output: ifconfig
- JC Convert Command Output: key value pairs
- JC Convert Command Output: last
- JC Convert Command Output: ls
- JC Convert Command Output: mount
- JC Convert Command Output: netstat
- JC Convert Command Output: ping
- JC Convert Command Output: ps
- JC Convert Command Output: route
- JC Convert Command Output: sha256sum
- JC Convert Command Output: tracepath
- JC Convert Command Output: uname
- JC Convert Command Output: uptime
- JC Convert Command Output: w

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
