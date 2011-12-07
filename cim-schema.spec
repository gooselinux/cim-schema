#
# spec file for package cim-schema
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon.
#
# The license for this spec file is the MIT/X11 license:
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

# norootforbuild

Name:           cim-schema
Url:            http://www.dmtf.org/
Summary:        Common Information Model (CIM) Schema
Version:        2.22.0
Release:        2.1%{?dist}
Group:          Development/Libraries
License:        DMTF
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        http://www.dmtf.org/standards/cim/cim_schema_v2220/cim_schema_%{version}Experimental-MOFs.zip
Source1:        http://www.dmtf.org/standards/cim/cim_schema_v2220/cim_schema_%{version}Experimental-Doc.zip
Source2:        loadmof.sh
Source3:        rmmof.sh
Source4:        LICENSE
BuildArch:      noarch

%package docs
Summary:        Common Information Model (CIM) Schema documentation
Group:          Documentation


%description
Common Information Model (CIM) is a model for describing overall
management information in a network or enterprise environment. CIM
consists of a specification and a schema. The specification defines the
details for integration with other management models. The schema
provides the actual model descriptions.



Authors:
--------
    DTMF <http://www.dmtf.org/about/contact>

%description docs
Common Information Model (CIM) schema documentation.

%prep
%setup -q -T -a 1 -c -n %{name}-%{version}-docs
%setup -q -T -a 0 -c -n %{name}-%{version}
cp -a %{SOURCE4} ..

%build
%install
MOFDIR=%{_datadir}/mof
CIMDIR=$MOFDIR/cimv%{version}
%__rm -rf $RPM_BUILD_ROOT
for i in `find . -name "*.mof"`; do
  sed -i -e 's/\r//g' $i
done
install -d $RPM_BUILD_ROOT/$CIMDIR
chmod -R go-wx .
chmod -R a+rX .
%__mv * $RPM_BUILD_ROOT/$CIMDIR/
ln -s cimv%{version} $RPM_BUILD_ROOT/$MOFDIR/cim-current
ln -s cim_schema_%{version}.mof $RPM_BUILD_ROOT/$MOFDIR/cim-current/CIM_Schema.mof
install -d $RPM_BUILD_ROOT/usr/bin
install -m 755 %{S:2} $RPM_BUILD_ROOT/usr/bin/
install -m 755 %{S:3} $RPM_BUILD_ROOT/usr/bin/

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%dir /usr/share/mof
%dir /usr/share/mof/cimv%{version}
/usr/share/mof/cimv%{version}/*
/usr/share/mof/cim-current
/usr/bin/loadmof.sh
/usr/bin/rmmof.sh
%doc ../LICENSE

%files docs
%defattr(-, root, root)
%doc ../%{name}-%{version}-docs/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.22.0-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Matt Domsch <Matt_Domsch@dell.com> - 2.22.0-1.fc12
- add dist tag

* Tue Jul 14 2009 Matt Domsch <Matt_Domsch@dell.com> - 2.22.0-1
- spec license change to MIT per Novell
- remove BR: unzip, it's in the default buildroot already
- add MIT license to spec file

* Wed May 20 2009 Matt Domsch <Matt_Domsch@dell.com> - 2.21.0-1
- upgrade to v2.22.0

* Thu Oct 23 2008 Matt Domsch <Matt_Domsch@dell.com> - 2.19.1-1
- Upgraded to cimv2.19.1Experimental
- now meets Fedora packaging guidelines too
- added -docs subpackage
* Wed May 14 2008 bwhiteley@suse.de
- Upgraded to cimv2.18Experimental
* Thu Jan 17 2008 bwhiteley@suse.de
- Fixed order of includes so that it will import in pegasus.
* Tue Jan 08 2008 bwhiteley@suse.de
- Updated to cimv2.17Experimental (#341800)
* Wed Nov 28 2007 bwhiteley@suse.de
- Updated to cimv2.16Experimental (#341800)
  Remove carriage returns from MOF files.
  Fix broken comment blocks in 2.16 schema.
* Thu Mar 29 2007 bwhiteley@suse.de
- Added unzip to BuildRequires
* Tue Mar 27 2007 bwhiteley@suse.de
- Fixed inclusion of missing file (#258187)
* Tue Mar 13 2007 bart@novell.com
- Added some classes from 2.15 preliminary needed for Xen
  providers (#228365)
* Fri Jan 19 2007 bwhiteley@suse.de
- update to schema version 2.14 (#228365)
* Mon Jan 08 2007 bwhiteley@suse.de
- Combine all qualifiers back into one file (#232667)
* Tue Dec 19 2006 bwhiteley@suse.de
- added loadmof.sh script. (#228349)
* Wed Dec 13 2006 bwhiteley@suse.de
- Updated to schema version cimv2.13.1 (#228365)
* Fri Oct 06 2006 bwhiteley@suse.de
- Updated to schema version cimv2.13
* Mon May 08 2006 bwhiteley@suse.de
- Updated to schema version cimv2.12, required for SMASH 1.0
  compliance (#173777)
* Fri May 05 2006 bwhiteley@suse.de
- removed non-ascii char from CIM_DNSSettingData.mof (was breaking
  some XML parsers) (#172939)
* Fri Feb 10 2006 bwhiteley@suse.de
- fixed execute bit on directories (#149992)
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Jan 17 2006 bwhiteley@suse.de
- Added a symlink cim-current so other packages don't have to hard-
  code cim schema versions.
* Tue Jan 10 2006 bwhiteley@suse.de
- Update to v2.11 Experimental.
- Moved MOFs under /usr/share/mof
* Thu Jan 13 2005 nashif@suse.de
- Update to v2.9 Final
* Tue Oct 12 2004 nashif@suse.de
- Update with cim v2.9
* Tue Feb 17 2004 nashif@suse.de
- Fixed directory permissions
- build as normal user
* Mon Feb 16 2004 nashif@suse.de
- Updated to 2.8 final
* Thu Nov 27 2003 nashif@suse.de
- Initial Release
