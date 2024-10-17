%define upstream_name    Wx-Scintilla
%define upstream_version 0.39

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	A list of Wx::Scintilla constants
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Wx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Alien::wxWidgets)
BuildRequires:	perl(ExtUtils::XSpp) >= 0.160.200
BuildRequires:	perl(Module::Build) >= 0.360.0
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Wx)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	wxgtku2.8-devel
%description
While we already have a good scintilla editor component support via
Wx::StyledTextCtrl in Perl, we already suffer from an older scintilla
package and thus lagging Perl support in the popular Wx Scintilla
component. wxWidgets the http://wxwidgets.org manpage has a *very slow*
release timeline. Scintilla is a contributed project which means it will
not be the latest by the time a new wxWidgets distribution is released. And
on the scintilla front, the Perl 5 lexer is not 100% bug free even and we
do not have any kind of Perl 6 support in Scintilla.

The ambitious goal of this project is to provide fresh Perl 5 and maybe 6
support in the Wx manpage while preserving compatibility with
Wx::StyledTextCtrl and continually contribute it back to Scintilla project.

Note: You cannot load Wx::STC and Wx::Scintilla in the same application.
They are mutually exclusive. The wxSTC_... events are handled by one
library or the other.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

#check
# requires display
#./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes META.json META.yml MYMETA.yml README XS
%{_mandir}/man3/*
%{perl_vendorlib}/*

