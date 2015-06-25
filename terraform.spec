Name:           terraform
Version:        0.5.3
Release:        1%{?dist}
Summary:        Terraform provides a common configuration to launch cloud-based infrastructure.
Group:          Applications/System
License:        MPLv2.0
URL:            https://terraform.io/
Source0:        https://dl.bintray.com/mitchellh/%{name}/%{name}_%{version}_linux_amd64.zip
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
%endif

%description
Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as custom in-house solutions.
Configuration files describe to Terraform the components needed to run a single application or your entire datacenter. Terraform generates an execution plan describing what it will do to reach the desired state, and then executes it to build the described infrastructure. As the configuration changes, Terraform is able to determine what changed and create incremental execution plans which can be applied.

%prep
%setup -q -c

%install
mkdir -p %{buildroot}/%{_bindir}
cp %{name}* %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/%{name}*

%doc

%changelog
* Mon May 11 2015 dan phrawzty <phrawzty@mozilla.com>
- bump to v0.5.0
* Wed May 06 2015 dan phrawzty <phrawzty@mozilla.com>
- init v0.4.2
