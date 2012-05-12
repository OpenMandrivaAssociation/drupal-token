%define modname		token
%define drupal_version	7
%define module_version	1.0
%define version		%{drupal_version}.x.%{module_version}
%define tarname		%{modname}-%{drupal_version}.x-%{module_version}

Name:		drupal-%{modname}
Summary:	Token module for Drupal
Version:	%{version}
Release:	1
License:	GPLv2+
Group:		Networking/WWW
URL:		https://drupal.org/project/%{modname}
Source0:	http://ftp.drupal.org/files/projects/%{tarname}.tar.gz
Source1:	%{name}.rpmlintrc
Requires:	drupal >= %{drupal_version}
Requires:	drupal < %{lua: print(rpm.expand("%{drupal_version}")+1)}
BuildArch:	noarch

%description
Tokens are small bits of text that can be placed into larger documents via
simple placeholders, like %%site-name or [user]. The Token module provides
a central API for modules to use these tokens, and expose their own token
values.

Note that Token module doesn't provide any visible functions to the user on its
own, it just provides token handling services for other modules.

The basic token API is now a part of Drupal 7! Unfortunately, other things like
the a browsable token UI, and field & profile tokens did not make it into core
and will be supported here for Drupal 7.

%prep
%setup -q -n %{modname}

%build

%install
%__install -d -m 0755 %{buildroot}%{_var}/www/drupal/modules/
cp -a . %{buildroot}%{_var}/www/drupal/modules/%{modname}
rm -f %{buildroot}%{_var}/www/drupal/modules/%{modname}/*.txt

%files
%{_var}/www/drupal/modules/%{modname}
%doc README.txt
