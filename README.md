## AMAZON-SSM-AGENT-SELINUX POLICY

This is the SELinux policy for AWS SSM agent. Install this policy to confine your SSM agent processes.

## Installation instructions

To build and install the SELinux policy, make sure that SELinux is in permissive or enforcing mode in `/etc/selinux/config` file and reboot the instance:
```
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
SELINUX=enforcing
# SELINUXTYPE= can take one of three two values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy. Only selected processes are protected. 
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted
```

Run the following commands:
```
sudo yum install policycoreutils-devel rpm-build git
git clone https://github.com/aws/amazon-ssm-agent-selinux.git
cd amazon-ssm-agent-selinux
chmod +x amazon_ssm_agent.sh
sudo ./amazon_ssm_agent.sh
```
Reboot the instance or restart the SSM Agent service using:

```
sudo systemctl restart amazon-ssm-agent.service

ps -efZ | grep -i amazon

system_u:system_r:amazon_ssm_agent_t:s0 root 5665  1  0 00:15 ?        00:00:02 /usr/bin/amazon-ssm-agent
system_u:system_r:amazon_ssm_agent_t:s0 root 5746 5665  0 00:15 ?      00:00:02 /usr/bin/ssm-agent-worker

```

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the GNU GPL v2 License.

