Name: trace-cmd
Version: 2.7.0
Release: 3%{?dist}
License: GPLv2 and LGPLv2+
Summary: A user interface to Ftrace

Group: Development/Tools
URL: http://www.kernel.org/pub/linux/analysis/trace-cmd/
Source: %{URL}/%{name}-%{version}.tar.bz2

# Patches
Patch1: 0001-trace-cmd-Figure-out-the-arch-and-install-library-to.patch
Patch2: Add-trace-cmd-flightrecorder-service.patch
Patch3: Various-fixes-for-trace-cmd-flightrecorder-systemd.patch
Patch4: trace-cmd-Optimize-how-pid-filters-are-expressed.patch
Patch5: trace-cmd-Add-no-filter-option-to-not-filter-out-rec.patch
Patch6: tools-lib-traceevent-Fix-missing-equality-check.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: xmlto
BuildRequires: asciidoc
BuildRequires: mlocate
BuildRequires: python-devel
BuildRequires: python-libs
BuildRequires: swig
BuildRequires: systemd
BuildRequires: audit-libs-devel

%description
The trace-cmd utility is a user interface to Ftrace.
Instead of needing to use the debugfs directly, trace-cmd will handle of
setting of options and tracers and will record into a data file.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1


%build
# MANPAGE_DOCBOOK_XSL define is hack to avoid using locate
MANPAGE_DOCBOOK_XSL=`rpm -ql docbook-style-xsl | grep manpages/docbook.xsl`
make MANPAGE_DOCBOOK_XSL=$MANPAGE_DOCBOOK_XSL doc
make CFLAGS="-g -Wall -D_GNU_SOURCE -fstack-protector-strong" all

%global libdir %{_lib}

%install
rm -Rf %{buildroot}
mkdir -p %{buildroot}/%{_unitdir}/
mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig/
mkdir -p %{buildroot}/%{_udevrulesdir}
mkdir -p %{buildroot}/%{_libdir}/%{name}/python/
install -p -m 644 trace-cmd.service %{buildroot}/%{_unitdir}/
install -p -m 644 trace-cmd.conf %{buildroot}/%{_sysconfdir}/sysconfig/
install -p -m 644 98-trace-cmd.rules %{buildroot}/%{_udevrulesdir}/
make DESTDIR=%{buildroot} prefix=/usr libdir=/usr/%{libdir} install install_libs install_doc
install -p event-viewer.py %{buildroot}/%{_libdir}/%{name}/python/
install -p tracecmd.py %{buildroot}/%{_libdir}/%{name}/python/
install -p tracecmdgui.py %{buildroot}/%{_libdir}/%{name}/python/

%clean
make clean doc_clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING COPYING.LIB README
%{_bindir}/trace-cmd
%{_libdir}/%{name}/plugins/*
%{_libdir}/%{name}/python/*
%{_datadir}/kernelshark/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_unitdir}/trace-cmd.service
%{_sysconfdir}/sysconfig/trace-cmd.conf
%{_sysconfdir}/bash_completion.d/trace-cmd.bash
%{_includedir}/%{name}/event-parse.h
%{_includedir}/%{name}/trace-cmd.h
%{_libdir}/libparsevent.so
%{_libdir}/libtracecmd.so
%{_udevrulesdir}/98-trace-cmd.rules


%changelog
* Wed Apr 24 2019 John Kacur <jkacur@redhat.com> - 2.7-3
- Fix missing equality check
Resolves: rhbz#1702450

* Tue Apr 23 2019 John Kacur <jkacur@redhat.com> - 2.7-2
- Optimize how pid filters are expresssed
- Add a --no-filter option
Resolves: rhbz#1472631

* Mon Feb 11 2019 John Kacur <jkacur@redhat.com> - 2.7-1
- Rebase to trace-cmd-2.7
Resolves: rhbz#1655111

* Tue Jan 15 2019 John Kacur <jkacur@redhat.com> - 2.6.1-1
- Rebase to trace-cmd-2.6.1, drop unnecessary patches
Resolves: rhbz#1509259

* Mon Nov 06 2017 John Kacur <jkacur@redhat.com> - 2.6.0-10
- parse-events: Fix missing break in pevent_filter_clear
Resolves: rhbz#1509236

* Mon Aug 28 2017 John Kacur <jkacur@redhat.com> - 2.6.0-9
- add trace-cmd-record-Fix-filtering-when-using-set_event_pid_part2
Resolves: rhbz#1480770

* Thu May 04 2017 John Kacur <jkacur@redhat.com> - 2.6.0-8
- trace-cmd record: Fix filtering when using set_event_pid
Resolves: rhbz#1447927

* Fri Apr 28 2017 John Kacur <jkacur@redhat.com> - 2.6.0-7
- Updated to latest upstream, which among many fixes also includes
- external library for other programs to link to trace-cmd
- bash completion
Resolves: rhbz#1445825

* Thu Apr 06 2017 John Kacur <jkacur@redhat.com> - 2.6.0-6
- tools lib traceevent: Do not reassign parg after collapse_tree
Resolves: rhbz#1379506

* Tue Mar 21 2017 John Kacur <jkacur@redhat.com> - 2.6.0-5
- Fix segmentation fault in trace-snapshot
Resolves: rhbz#1389223

* Fri Jul 15 2016 John Kacur <jkacur@redhat.com> - 2.6.0-3
- Prevent trace-cmd-record crashes if -f is used before -e event
Resolves: rhbz#1249191

* Mon Jun 27 2016 John Kacur <jkacur@redhat.com> - 2.6.0-2
- Remove unncessary old patches, and reactivate needed ones.
Resolves: rhbz#1219852

* Wed Jun 22 2016 John Kacur <jkacur@redhat.com> - 2.6.0-1
Resolves: rhbz#1219852

* Thu Aug 13 2015 John Kacur <jkacur@redhat.com> - 2.2.2-4
- trace-cmd-Fix-missing-n-in-output-for-newline
Resolves: rhbz#1238524

* Tue Jun 30 2015 John Kacur <jkacur@redhat.com> - 2.2.2-3
- Various-fixes-for-trace-cmd-flightrecorder-systemd
Resolves: rhbz#1049701

* Thu Jun 04 2015 John Kacur <jkacur@redhat.com> - 2.2.2-2
- Add trace-cmd flightrecorder services
Resolves: rhbz#1049701

* Wed May 13 2015 John Kacur <jkacur@redhat.com> - 2.2.2-1
- Update to trace-cmd-v2.2.2 which includes the following fixes
- trace-input: Init kbuf back to NULL after free kbuf
- kernelshark: Use ull annotation for 64bit numbers
Resolves: rhbz#1219847

* Fri May 08 2015 John Kacur <jkacur@redhat.com> - 2.2.1-8
- Remove patches from tar file, and apply them explicitly in the spec file
- trace-split-Do-not-allow-spliting-of-latency-tracers.patch
Resolves: rhbz#1198942

* Wed Sep 10 2014 Dan Horák <dhorak@redhat.com> - 2.2.1-7
- fix build for 64-bit arches
- Resolves: #1125701

* Wed Mar 12 2014 John Kacur <jkacur@redhat.com> - 2.2.1-6
- Add aarch64 to list of arches that require lib64 (1028585)
Resolves: rhbz#1028585

* Wed Mar 05 2014 John Kacur <jkacur@redhat.com> - 2.2.1-5
- Add -fstack-protector-stack flag (1070800)
Resolves: rhbz#1070800

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 2.2.1-4
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.2.1-3
- Mass rebuild 2013-12-27

* Thu Aug 22 2013 John Kacur <jkacur@redhat.com> - 2.2.1-2
- Various fixes for problems discovered by rpmlint
- Update the address of FSF in various files
- Install documentation and non-script python files at mode 644

* Mon May 13 2013 John Kacur <jkacur@redhat.com> - 2.2.1-1
- Rebased to 2.2.1
- Added libdir variable to Makefile for arch x86_64 to create libs in lib64

* Tue Nov 27 2012 John Kacur <jkacur@redhat.com> - 2.0.2-9
- Changed the spec file to cope with new file layout

* Mon Nov 26 2012 John Kacur <jkacur@redhat.com>
- Rebasing to trace-cmd-2.0.2

* Wed Mar 7 2012 John Kacur <jkacur@redhat.com>
- Rebasing to trace-cmd-1.0.5
- Backported commits for -i option.
Resolves:bz632061

* Mon Jul 5 2010 John Kacur <jkacur@redhat.com>
- Rebasing to trace-cmd-1.0.4

* Wed Jun 16 2010 John Kacur <jkacur@redhat.com>
- Rebasing to trace-cmd-1.0.2
- Added parse-events-Do-not-fail-on-FORMAT-TOO-BIG-event-err.patch
- Added trace-cmd-Prevent-latency-tracer-plugins-from-doing-.patch
- Added trace-cmd-Prevent-print_graph_duration-buffer-overfl.patch

* Wed Jun 9 2010 John Kacur <jkacur@redhat.com>
- Added trace-cmd-Makefile-EXTRAVERSION-should-be-set-withou.patch
- Added trace-cmd-Makefile-use-a-substitution-reference.patch
- add-DESTDIR-to-make.patch
- Related: rhbz599507

* Fri Jun 4 2010 John Kacur <jkacur@redhat.com>
- Updating to trace-cmd-1.0.1
- Related: rhbz599507

* Wed Apr 21 2010 John Kacur <jkacur@redhat.com>
- Using trick from William Cohen to avoid the "locate" problem.

* Fri Apr 16 2010 John Kacur <jkacur@redhat.com>
- Update the source to the 1.0.0 version
- Many fixes to the spec file.

* Mon Apr 12 2010 William Cohen <wcohen@redhat.com>
- Include manpages in the package.

* Fri Apr 9 2010 John Kacur <jkacur@redhat.com>
- disabled #patch01
- Updated the trace-cmd source
- Changed version to 0.7.0
- Added bogus patch to satisfy rpm requirements
- Related:bz519630

* Mon Mar 15 2010 John Kacur <jkacur@redhat.com>
- disabled trace-cmd_rusage.patch
- Updated the trace-cmd source
- Related:bz519630

* Fri Nov 16 2007 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.0-1%{?dist}
- Initial packaging
- Added a patch to display rusage information
