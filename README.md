## AMAZON-SSM-AGENT-SELINUX POLICY

This is the SELinux policy for Amazon SSM agent. Install this policy to confine your SSM agentt processes.

## Installation instructions

To build and Install the SELinux policy, make sure that SELinux is in permissive or enforcing mode in `/etc/selinux/config` file

Run the following commands:
```
sudo yum install policycoreutils-devel rpm-build git
git clone https://github.com/aws/amazon-ssm-agent-selinux.git
cd amazon-ssm-agent-selinux
chmod +x amazon_ssm_agent.sh
./amazon_ssm_agent.sh
```

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the GNU GPL v2 License.

