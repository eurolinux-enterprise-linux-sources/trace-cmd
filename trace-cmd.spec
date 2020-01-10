Name: trace-cmd
Version: 2.2.4
Release: 4%{?dist}
License: GPLv2 and LGPLv2+
Summary: trace-cmd is a user interface to Ftrace

Group: Development/Tools
URL: http://www.kernel.org/pub/linux/analysis/trace-cmd/
Source: %{URL}/%{name}-%{version}.tar.bz2
Patch1: trace-cmd-Makefile-Determine-whether-to-install-to-l.patch
Patch2: trace-cmd-record-crashes-if-f-is-used-before-e-event.patch
Patch3: trace-cmd-don-t-call-free-on-tracing-and-path-more-t.patch
Patch4: trace-cmd-trace-cmd.c-Don-t-deref-re-if-it-is-NULL.patch
Patch5: trace-cmd-trace-recorder.c-Prevent-free-of-unitializ.patch
Patch6: trace-cmd-trace-util.c-Prevent-resource-leak-by-clos.patch
Patch7: trace-cmd-split-Do-not-allow-spliting-of-latency-tra.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: xmlto
BuildRequires: asciidoc
BuildRequires: mlocate
BuildRequires: python-devel
BuildRequires: python-libs
BuildRequires: swig

%description
trace-cmd is a user interface to Ftrace. Instead of needing to use the
debugfs directly, trace-cmd will handle of setting of options and
tracers and will record into a data file.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
# MANPAGE_DOCBOOK_XSL define is hack to avoid using locate
MANPAGE_DOCBOOK_XSL=`rpm -ql docbook-style-xsl | grep manpages/docbook.xsl`
make MANPAGE_DOCBOOK_XSL=$MANPAGE_DOCBOOK_XSL all doc

%install
rm -Rf %{buildroot}
make DESTDIR=%{buildroot} prefix=%{_prefix} install install_doc

%clean
make clean doc_clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING COPYING.LIB README
%{_bindir}/trace-cmd
%{_libdir}/%{name}
%{_datadir}/kernelshark/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
* Tue Sep 13 2016 John Kacur <jkacur@redhat.com> - 2.2.4-4
- Do not allow spliting of latency tracers
Resolves: rhbz#1328692

* Tue Jan 19 2016 John Kacur <jkacur@redhat.com> - 2.2.4-3
- trace-cmd-don-t-call-free-on-tracing-and-path-more-t.patch
- trace-cmd-trace-cmd.c-Don-t-deref-re-if-it-is-NULL.patch
- trace-cmd-trace-recorder.c-Prevent-free-of-unitializ.patch
- trace-cmd-trace-util.c-Prevent-resource-leak-by-clos.patch
Resolves: rhbz#1288579

* Wed Nov 18 2015 John Kacur <jkacur@redhat.com> - 2.2.4-2
- trace-cmd: record crashes if -f is used before -e event
Resolves: rhbz#1249194

* Fri Nov 13 2015 John Kacur <jkacur@redhat.com> - 2.2.4-1
- Upgrade to trace-cmd-v2.2.4
Resolves: rhbz#1218670

* Thu Mar 27 2014 John Kacur <jkacur@redhat.com> - 1.0.5-11
- Rework spec to use apply patches separate from upstream
- trace-cmd-Add-checks-for-invalid-pointers-to-fix-seg.patch (879814)
Resolves:bz879814

* Wed Dec 12 2012 John Kacur <jkacur@redhat.com> - 1.0.5-10
- trace-cmd: Do not call stop_threads() if doing latency tracing
Resolves:bz879792

* Tue Oct 2 2012 John Kacur <jkacur@redhat.com> - 1.0.5-9
-  trace-cmd: Allow more than one pid to be traced
Resolves:bz838746

* Mon Sep 10 2012 John Kacur <jkacur@redhat.com> - 1.0.5-8
- trace-cmd: Use splice to filter out rest of buffer {746656}
- trace-cmd: Do not use threads for extract {746656}
Resolves:bz746656

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
