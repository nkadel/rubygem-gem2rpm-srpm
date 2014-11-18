# Generated from gem2rpm-0.10.1.gem by gem2rpm -*- rpm-spec -*-
%global gemname gem2rpm

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: Generate rpm specfiles from gems
Name: rubygem-%{gemname}
Version: 0.10.1
Release: 0.1%{?dist}
Group: Development/Languages
License: GPLv2
URL: https://github.com/lutter/gem2rpm/
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Generate source rpms and rpm spec files from a Ruby Gem. 
The spec file tries to follow the gem as closely as possible.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -pa .%{gemdir}/* \
        %{buildroot}%{gemdir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%files
%dir %{geminstdir}
%{_bindir}/gem2rpm
%{geminstdir}/bin
%{geminstdir}/lib
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
# Added for template .erb files
%{gemdir}/gems/%{gemname}-%{version}/templates

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/AUTHORS
%doc %{geminstdir}/README
%doc %{geminstdir}/LICENSE


%changelog
* Mon Nov 17 2014 Nico Kadel-Garcia <nkadel@gmail.com> - 0.10.1-1
- Initial package
- Set License to GPLv2 manually
- Add templates to list of files

