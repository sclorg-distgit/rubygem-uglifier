%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from uglifier-1.2.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name uglifier
%global rubyabi 1.9.1

Summary: Ruby wrapper for UglifyJS JavaScript compressor
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.6
Release: 4.sc1%{?dist}
Group: Development/Languages
# Uglifier itself is MIT
# the bundled JavaScript from UglifyJS is BSD
License: MIT and BSD
URL: http://github.com/lautis/uglifier
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems) 
Requires: %{?scl_prefix}rubygem(execjs) >= 0.3.0
Requires: %{?scl_prefix}rubygem(multi_json) => 1.3
Requires: %{?scl_prefix}rubygem(multi_json) < 2
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(execjs) >= 0.3.0
BuildRequires: %{?scl_prefix}rubygem(json)
BuildRequires: %{?scl_prefix}rubygem(multi_json) => 1.3
BuildRequires: %{?scl_prefix}rubygem(multi_json) < 2
BuildRequires: %{?scl_prefix}rubygem(rspec)
BuildRequires: %{?scl_prefix}rubygem(therubyracer)
%{?scl:BuildRequires: scldevel(v8)}
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Ruby wrapper for UglifyJS JavaScript compressor.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} %{scl_v8} "}
rspec spec
%{?scl:"}
popd


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/build.js
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec
%doc %{gem_instdir}/VERSION
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Mon Feb 17 2014 Josef Stribny <jstribny@redhat.com> - 1.2.6-4
- Depend on scldevel(v8) virtual provide
  - Resolves: rhbz#1065887

* Thu Nov 28 2013 Vít Ondruch <vondruch@redhat.com> - 1.2.6-3
- Build against v8314 SCL.

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.6-2
- Imported from Fedora again.

* Mon Jul 16 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.6-1
- Initial package
