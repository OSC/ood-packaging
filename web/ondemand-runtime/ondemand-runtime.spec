%global scl ondemand
%global scl_name_base %scl
%global _scl_prefix /opt/ood
%scl_package %scl
%global nfsmountable 0

Name:      ondemand-runtime
Version:   1.4
Release:   2%{?dist}
Summary:   Package that handles %{scl} Software Collection.
License:   MIT

BuildRequires:  scl-utils-build
Requires:       scl-utils
Requires:       rh-ruby24-runtime
Requires:       rh-nodejs6-runtime
Requires:       rh-git29-runtime
Requires:       httpd24-runtime

%description
Package shipping essential scripts to work with %{scl} Software Collection.

%package -n ondemand-build
Summary: Package shipping basic build configuration
Requires: scl-utils-build

%description -n ondemand-build
Package shipping essential configuration macros to build %{scl} Software Collection.

%package -n ondemand-scldevel
Summary: Package shipping development files for %{scl}

%description -n ondemand-scldevel
Package shipping development files, especially useful for development of
packages depending on %{scl} Software Collection.

%prep
%setup -c -T

%install
%scl_install
cat >> %{buildroot}%{_scl_scripts}/enable << EOF
. scl_source enable httpd24 rh-ruby24 rh-nodejs6 rh-git29
export PATH="%{_bindir}:%{_sbindir}\${PATH:+:\${PATH}}"
export LD_LIBRARY_PATH="%{_libdir}\${LD_LIBRARY_PATH:+:\${LD_LIBRARY_PATH}}"
export MANPATH="%{_mandir}:\${MANPATH:-}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig\${PKG_CONFIG_PATH:+:\${PKG_CONFIG_PATH}}"
EOF

cat >> %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel << EOF
%%scl_%{scl_name_base} %{scl}
%%scl_prefix_%{scl_name_base} %{scl_prefix}
EOF

%files -f filelist
%scl_files

%files -n ondemand-build
%{_root_sysconfdir}/rpm/macros.%{scl}-config

%files -n ondemand-scldevel
%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel

%changelog
* Tue Jan 15 2019 Trey Dockendorf <tdockendorf@osc.edu> 1.4-1
- new package built with tito
