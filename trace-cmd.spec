Name: trace-cmd
Version: 2.6.0
Release: 10%{?dist}
License: GPLv2 and LGPLv2+
Summary: A user interface to Ftrace

Group: Development/Tools
URL: http://www.kernel.org/pub/linux/analysis/trace-cmd/
Source: %{URL}/%{name}-%{version}.tar.bz2

Patch1: 0001-event-parse-Fix-time-stamp-format-problem.patch
Patch2: 0002-event-parse-Use-USECS_PER_SEC-instead-of-hardcoded-n.patch
Patch3: 0003-trace-cmd-Leave-out-absolute-addresses-to-fix-bogus-.patch
Patch4: 0004-event-parse-Fix-second-increment.patch
Patch5: 0005-trace-cmd-listen-Remove-malloc_or_die.patch
Patch6: 0006-trace-cmd-hook-Remove-malloc_or_die.patch
Patch7: 0007-trace-cmd-Remove-malloc_or_die-and-other-die-from-tr.patch
Patch8: 0008-trace-cmd-Remove-die-from-insufficient-memory-in-tra.patch
Patch9: 0009-trace-cmd-profiler-Removed-malloc_or_die.patch
Patch10: 0010-trace-cmd-Remove-malloc_or_die-form-trace-read.c.patch
Patch11: 0011-trace-cmd-Remove-malloc_or_die-from-trace-record.c.patch
Patch12: 0012-trace-cmd-Check-the-return-of-create_instance.patch
Patch13: 0013-trace-cmd-Remove-malloc_or_die-from-trace-recorder.c.patch
Patch14: 0014-trace-cmd-split-Remove-malloc_or_die.patch
Patch15: 0015-trace-cmd-stat-Remove-malloc_or_die.patch
Patch16: 0016-trace-cmd-Remove-malloc_or_die-from-trace-cmd.c.patch
Patch17: 0017-trace-cmd-Change-trace-util.c-to-not-die-on-errors.patch
Patch18: 0018-parse-events-Fix-output-of-llu-for-64-bit-values-rea.patch
Patch19: 0019-trace-cmd-Never-update-saved-files-when-keep-is-set-.patch
Patch20: 0020-trace-cmd-Truncate-files-when-writing-to-them.patch
Patch21: 0021-trace-cmd-Fix-trace-record.c-with-non-ptrace-compile.patch
Patch22: 0022-trace-cmd-Use-set_event_pid-when-available.patch
Patch23: 0023-trace-cmd-If-event-fork-option-exists-use-it-instead.patch
Patch24: 0024-tools-lib-traceevent-Allow-setting-an-alternative-sy.patch
Patch25: 0025-tools-lib-traceevent-Support-function-__get_dynamic_.patch
Patch26: 0026-tools-lib-traceevent-Factor-out-and-export-print_eve.patch
Patch27: 0027-tools-lib-traceevent-Support-ps-pS.patch
Patch28: 0028-tools-lib-traceevent-Fix-string-handling-in-heteroge.patch
Patch29: 0029-tools-lib-traceevent-Fix-output-of-llu-for-64-bit-va.patch
Patch30: 0030-tools-lib-traceevent-Add-checks-for-returned-EVENT_E.patch
Patch31: 0031-irq_poll-make-blk-iopoll-available-outside-the-block.patch
Patch32: 0032-kernelshark-Clean-up-some-of-the-code-warnings.patch
Patch33: 0033-kernelshark-Add-event-and-box-info-struct-to-plot-st.patch
Patch34: 0034-trace-graph-Have-debug-resolution-16-digits.patch
Patch35: 0035-kernelshark-Time-the-drawing-of-the-graph.patch
Patch36: 0036-kernelshark-Don-t-draw-overlapping-event-lines.patch
Patch37: 0037-kernelshark-Pass-the-calculation-of-convert_time_to_.patch
Patch38: 0038-kernelshark-Do-not-calculate-the-graph-the-first-tim.patch
Patch39: 0039-trace-cmd-Have-n-add-to-set_graph_notrace-if-functio.patch
Patch40: 0040-kernelshark-Filter-out-preempt-from-running-sched-sw.patch
Patch41: 0041-kernelshark-Show-event-data.patch
Patch42: 0042-event-parse-Add-retrieval-of-preempt-count-and-laten.patch
Patch43: 0043-trace-cmd-report-Add-I-option-to-remove-interrupts-f.patch
Patch44: 0044-trace-cmd-report-Add-S-option-to-remove-softirqs-fro.patch
Patch45: 0045-kerenshark-Have-task-plots-show-when-they-are-in-int.patch
Patch46: 0046-trace-cmd-report-Add-ts-offset-to-add-to-timestamps-.patch
Patch47: 0047-trace-cmd-record-Add-ts-offset-for-timestamp-of-even.patch
Patch48: 0048-trace-cmd-report-Add-ts2secs-to-convert-cycles-into-.patch
Patch49: 0049-trace-cmd-Don-t-call-free-on-tracing-and-path-more-t.patch
Patch50: 0050-trace-cmd-Quiet-some-output-when-using-libtracecmd.patch
Patch51: 0051-trace-cmd-Filter-out-specific-pids.patch
Patch52: 0052-trace-cmd-profile-Fix-error-checking-of-find_and_upd.patch
Patch53: 0053-trace-cmd-profile-Handle-NULL-case-in-handle_fgraph_.patch
Patch54: 0054-tools-lib-traceevent-Implement-operation.patch
Patch55: 0055-tools-lib-traceevent-Add-operation-within-arg_num_ev.patch
Patch56: 0056-tools-lib-traceevent-Split-pevent_print_event-into-s.patch
Patch57: 0057-trace-cmd-report-Add-ts-diff-to-show-the-delta-betwe.patch
Patch58: 0058-trace-cmd-bash-Add-auto-complete-for-bash.patch
Patch59: 0059-trace-cmd-Install-trace-cmd.bash-when-installing.patch
Patch60: 0060-kernelshark-Have-irq-event-arrays-point-to-other-tha.patch
Patch61: 0061-kernelshark-Handle-freeing-of-int-arrays.patch
Patch62: 0062-trace-cmd-Add-bash-completion-for-e-p-l-n-g.patch
Patch63: 0063-trace-cmd-Keep-default-bash-completion-to-list-files.patch
Patch64: 0064-trace-cmd-listen-Apply-the-trace-msg-protocol-for-co.patch
Patch65: 0065-trace-cmd-listen-Update-the-V2-protocol-to-handle-ol.patch
Patch66: 0066-trace-cmd-msg-Use-poll-2-to-wait-for-a-message.patch
Patch67: 0067-trace-cmd-Replace-bufcpy-with-msgcpy-and-optcpy.patch
Patch68: 0068-trace-cmd-Make-msgcpy-and-optcpy-check-for-size.patch
Patch69: 0069-trace-cmd-Add-debug-option-to-tell-msg-protocol-not-.patch
Patch70: 0070-trace-cmd-listen-Add-a-pid-file-when-in-daemon-mode.patch
Patch71: 0071-trace-cmd-listen-Change-install-location-to-handle-u.patch
Patch72: 0072-trace-cmd-Always-use-var-run-and-var-lib.patch
Patch73: 0073-tools-lib-traceevent-Remove-redundant-CPU-output.patch
Patch74: 0074-trace-cmd-record-Fix-const-placement.patch
Patch75: 0075-trace-cmd-record-add-max-graph-depth-option.patch
Patch76: 0076-trace-cmd-Fix-reporting-of-unknown-SVM-exit-reasons.patch
Patch77: 0077-trace-cmd-Add-more-SVM-exit-reasons.patch
Patch78: 0078-trace-cmd-Introduce-tracecmd_peek_next_data.patch
Patch79: 0079-trace-cmd-Consolidate-tracecmd_-read-peak-_next_data.patch
Patch80: 0080-trace-cmd-Use-tracecmd_peek_next_data-in-fgraph_ent_.patch
Patch81: 0081-tools-lib-traceevent-Do-not-reassign-parg-after-coll.patch
Patch82: 0082-event-parse-Add-filter-on-task-CPU-id.patch
Patch83: 0083-trace-cmd-record-crashes-if-f-is-used-before-e-event.patch
Patch84: 0084-kernelshark-Fix-null-pointer-when-next-record-does-n.patch
Patch85: 0085-trace-graph-Do-not-show-interrupts-if-no-interrupt-e.patch
Patch86: 0086-trace-graph-Show-events-missed-in-cpu-plot.patch
Patch87: 0087-kernelshark-Add-infrastructure-to-allow-kernelshark-.patch
Patch88: 0088-trace-view-Place-focus-back-into-search-box-after-se.patch
Patch89: 0089-cpu.h-use-standard-types-instead-of-glib-s.patch
Patch90: 0090-trace-cmd-record-refactor-set_mask.patch
# Patch91: 0091-trace-cmd-Documentation-ignore-all-man-sections.patch
Patch92: 0092-trace-cmd-Add-page_map-for-entire-file.patch
Patch93: 0093-trace-cmd-listen-Make-sure-plog-messages-get-to-cons.patch
Patch94: 0094-trace-cmd-listen-Do-not-clean-up-in-signal-handler.patch
Patch95: 0095-trace-cmd-listen-Reuse-slots-in-client_pid-list.patch
Patch96: 0096-trace-cmd-listen-Free-pid_list-in-destroy_all_reader.patch
Patch97: 0097-trace-cmd-listen-Free-temp-files-in-put_together_fil.patch
Patch98: 0098-trace-cmd-listen-Simplify-adding-of-client_pids.patch
Patch99: 0099-trace-cmd-msg-Rewrote-a-lot-of-code-to-be-more-flexi.patch
Patch100: 0100-trace-cmd-msg-Consolidate-logic-of-allocating-reads-.patch
Patch101: 0101-trace-cmd-msg-Do-not-perform-read-when-expecting-no-.patch
Patch102: 0102-trace-cmd-Make-debug-a-global-variable.patch
Patch103: 0103-tracecmd-list-Add-debug-option.patch
Patch104: 0104-trace-cmd-msg-Remove-hook-for-telling-trace-msg.c-ab.patch
Patch105: 0105-trace-cmd-msg-Add-msg_write-helper-for-msg_do_write_.patch
Patch106: 0106-trace-cmd-list-Fix-the-error-message-to-show-the-wro.patch
Patch107: 0107-trace-cmd-Fix-file-pointer-leak-on-error-exit-of-tra.patch
Patch108: 0108-trace-cmd-Free-debug_str-on-error-exit-in-tracecmd_f.patch
Patch109: 0109-trace-cmd-Update-FSF-address-in-COPYING.LIB.patch
Patch110: 0110-tools-lib-traceevent-Use-str_error_r.patch
Patch111: 0111-tools-lib-traceevent-Add-correct-header-for-ipv6-def.patch
Patch112: 0112-trace-cmd-Move-die-and-friends-out-of-event-utils.h-.patch
Patch113: 0113-tools-lib-traceevent-Add-copyright-header.patch
Patch114: 0114-trace-cmd-Add-time64.h-to-be-like-the-kernel.patch
Patch115: 0115-trace-cmd-Move-trace-record-and-trace-restore-out-of.patch
Patch116: 0116-trace-cmd-add-install_libs-target-to-trace-cmd.patch
Patch117: 0117-trace-cmd-make-libtracecmd-a-little-more-library-fri.patch
Patch118: 0118-trace-cmd-add-a-function-to-create-a-top-instance.patch
Patch119: 0119-trace-cmd-add-global-functions-for-live-tracing.patch
Patch120: 0120-trace-cmd-allow-for-custom-show-and-handle-init.patch
Patch121: 0121-trace-cmd-Make-the-parse_-functions-tracecmd_parse_.patch
Patch122: 0122-trace-cmd-Do-not-initialize-profiler-if-it-isn-t-bei.patch
Patch123: 0123-trace-cmd-build-If-swig-is-not-installed-force-NO_PY.patch
Patch124: 0124-trace-cmd-Add-a-commented-single-quote-to-the-Makefi.patch
Patch125: 0125-trace-cmd-Fixup-more-bogus-symbol-resolutions.patch
Patch126: 0126-event-parse-Change-pevent_data_pc-to-pevent_data_pre.patch
Patch127: 0127-trace-cmd-Remove-include-of-string.h-from-event-util.patch
Patch128: 0128-tools-lib-traceevent-Initialize-lenght-on-OLD_RING_B.patch
Patch129: 0129-trace-cmd-Fix-segmentation-fault-in-trace-snapshot.patch
Patch130: 0130-plugin-python-fix-compiler-warning.patch
Patch131: 0131-plugin-python-check-asprintf-errors.patch
Patch132: 0132-trace-cmd-read-BUG-initialize-input_files-item-to-ze.patch
Patch133: 0133-trace-cmd-BUG-fix-malloc-pointer-validation.patch
Patch134: 0134-trace-view-Remove-unused-variable-selection.patch
Patch135: gpl-Update-the-address-of-the-FSF-in-the-header-of-s.patch
Patch136: Add-trace-cmd-flightrecorder-service.patch
Patch137: Various-fixes-for-trace-cmd-flightrecorder-systemd.patch
Patch138: trace-cmd-record-Fix-filtering-when-using-set_event_pid.patch
Patch139: trace-cmd-record-Fix-filtering-when-using-set_event_pid_part2.patch
Patch140: parse-events-Fix-missing-break-in-FALSE-case-of-peve.patch

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
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
# %patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch135 -p1
%patch136 -p1
%patch137 -p1
%patch138 -p1
%patch139 -p1
%patch140 -p1

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
install -p -m 644 trace-cmd.service %{buildroot}/%{_unitdir}/
install -p -m 644 trace-cmd.conf %{buildroot}/%{_sysconfdir}/sysconfig/
install -p -m 644 98-trace-cmd.rules %{buildroot}/%{_udevrulesdir}/
make DESTDIR=%{buildroot} prefix=/usr libdir=/usr/%{libdir} install install_libs install_doc

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
* Mon Nov 06 2017 John Kacur <jkacur@redhat.com> - 2.6.0-10
-parse-events: Fix missing break in pevent_filter_clear
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
