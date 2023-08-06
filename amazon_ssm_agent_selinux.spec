# vim: sw=4:ts=4:et


%define relabel_files() \
restorecon -R /usr/bin/amazon-ssm-agent; \
restorecon -R /etc/systemd/system/amazon-ssm-agent.service; \
restorecon -R /var/lib/amazon/ssm; \
restorecon -R /var/log/amazon/ssm; \

%define selinux_policyver 3.13.1-268

Name:   amazon_ssm_agent_selinux
Version:	1.0
Release:	1%{?dist}
Summary:	SELinux policy module for amazon_ssm_agent

Group:	System Environment/Base		
License:	GPLv2+	
# This is an example. You will need to change it.
URL:		https://github.com/aws/amazon-ssm-agent-selinux
Source0:	amazon_ssm_agent.pp
Source1:	amazon_ssm_agent.if
Source2:	amazon_ssm_agent_selinux.8


Requires: policycoreutils, libselinux-utils
Requires(post): selinux-policy-base >= %{selinux_policyver}, policycoreutils
Requires(postun): policycoreutils
Requires(post): amazon-ssm-agent
BuildArch: noarch

%description
This package installs and sets up the  SELinux policy security module for amazon_ssm_agent.

%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -d %{buildroot}%{_mandir}/man8/
install -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man8/amazon_ssm_agent_selinux.8
install -d %{buildroot}/etc/selinux/targeted/contexts/users/


%post
semodule -n -i %{_datadir}/selinux/packages/amazon_ssm_agent.pp
if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy
    %relabel_files

fi;
exit 0

%postun
if [ $1 -eq 0 ]; then
    semodule -n -r amazon_ssm_agent
    if /usr/sbin/selinuxenabled ; then
       /usr/sbin/load_policy
       %relabel_files

    fi;
fi;
exit 0

%files
%attr(0600,root,root) %{_datadir}/selinux/packages/amazon_ssm_agent.pp
%{_datadir}/selinux/devel/include/contrib/amazon_ssm_agent.if
%{_mandir}/man8/amazon_ssm_agent_selinux.8.*


%changelog
* Sun Dec 05 2022 Ayushman Dutta <> 1.0-1
- Initial version

