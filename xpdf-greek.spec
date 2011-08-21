Summary:	ISO-8859-7 encoding support for xpdf
Summary(pl.UTF-8):	Obsługa kodowania ISO-8859-7 dla xpdf
Name:		xpdf-greek
Version:	20110815
Release:	1
License:	GPL v2 or GPL v3
Group:		X11/Applications
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}-2011-aug-15.tar.gz
# Source0-md5:	2e988edf0c57def63717ee14bd6d30dd
URL:		http://www.foolabs.com/xpdf/
Requires(post,preun):	grep
Requires(post,preun):	xpdf
Requires(preun):	fileutils
Requires:	xpdf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xpdf language support packages include CMap files, text encodings,
and various other configuration information necessary or useful for
specific character sets. (They do not include any fonts.)
This package provides support files needed to use the Xpdf tools with
Greek PDF files.

%description -l pl.UTF-8
Pakiety wspierające języki Xpdf zawierają pliki CMap, kodowania oraz
różne inne informacje konfiguracyjne niezbędne bądź przydatne przy
określonych zestawach znaków (nie zawierają żadnych fontów).
Ten pakiet zawiera pliki potrzebne do używania narzędzi Xpdf z
greckimi plikami PDF.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xpdf

install *.unicodeMap $RPM_BUILD_ROOT%{_datadir}/xpdf
install *.nameToUnicode $RPM_BUILD_ROOT%{_datadir}/xpdf

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if [ ! -f /etc/xpdfrc ]; then
	echo 'unicodeMap	ISO-8859-7	/usr/share/xpdf/ISO-8859-7.unicodeMap' >> /etc/xpdfrc
	echo 'nameToUnicode			/usr/share/xpdf/Greek.nameToUnicode' >> /etc/xpdfrc
else
 if ! grep -q 'ISO-8859-7\.unicodeMap' /etc/xpdfrc; then
	echo 'unicodeMap	ISO-8859-7	/usr/share/xpdf/ISO-8859-7.unicodeMap' >> /etc/xpdfrc
 fi
 if ! grep -q 'Greek\.nameToUnicode' /etc/xpdfrc; then
	echo 'nameToUnicode		/usr/share/xpdf/Greek.nameToUnicode' >> /etc/xpdfrc
 fi
fi

%preun
if [ "$1" = "0" ]; then
	umask 022
	grep -v 'ISO-8859-7\.unicodeMap' /etc/xpdfrc > /etc/xpdfrc.new
	grep -v 'Greek\.nameToUnicode' /etc/xpdfrc.new > /etc/xpdfrc
	rm -f /etc/xpdfrc.new
fi

%files
%defattr(644,root,root,755)
%doc README add-to-xpdfrc
%{_datadir}/xpdf/Greek.nameToUnicode
%{_datadir}/xpdf/ISO-8859-7.unicodeMap
