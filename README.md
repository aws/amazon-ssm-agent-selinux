## AMAZON-SSM-AGENT-SELINUX POLICY

This is the SELinux policy for AWS SSM agent. Install this policy to confine your SSM agent processes.

## Installation instructions

Run the following commands:
```
sudo yum update
sudo yum install policycoreutils-devel rpm-build git
```

To build and install the SELinux policy, make sure that SELinux config file is in `permissive` or `enforcing` mode in `/etc/selinux/config` file:
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
Clone the repository, build and install using the commands below:

```
git clone https://github.com/aws/amazon-ssm-agent-selinux.git
cd amazon-ssm-agent-selinux
chmod +x amazon_ssm_agent.sh
sudo ./amazon_ssm_agent.sh
```
Reboot the instance and verify that your instance is in `enforcing` mode or `permissive` mode as chosen:

```
sudo sestatus

SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   enforcing
Mode from config file:          enforcing
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Max kernel policy version:      31

```

```

ps -efZ | grep -i amazon

system_u:system_r:amazon_ssm_agent_t:s0 root 5665  1  0 00:15 ?        00:00:02 /usr/bin/amazon-ssm-agent
system_u:system_r:amazon_ssm_agent_t:s0 root 5746 5665  0 00:15 ?      00:00:02 /usr/bin/ssm-agent-worker

```

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the GNU GPL v2 License.

