Summary:	ISO-8859-7 encoding support for xpdf
Summary(pl):	Wsparcie kodowania ISO-8859-7 dla xpdf
Name:		xpdf-greek
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}.tar.gz
URL:		http://www.foolabs.com/xpdf/
Requires:	xpdf
Requires(post,preun):	grep
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
The Xpdf language support packages include CMap files, text encodings,
and various other configuration information necessary or useful for
specific character sets. (They do not include any fonts.) 
This package provides support files needed to use the Xpdf tools with
Greek PDF files.

%description -l pl
Pakiety wspieraj±ce jêzyki Xpdf zawieraj± pliki CMap, kodowania oraz
ró¿ne inne informacje konfiguracyjne niezbêdne b±d¼ przydatne przy
okre¶lonych zestawach znaków. (Nie zawieraj± ¿adnych fontów).
Ten pakiet zawiera pliki potrzebne do u¿ywania narzêdzi Xpdf z
greckimi plikami PDF.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xpdf

install *.unicodeMap $RPM_BUILD_ROOT%{_datadir}/xpdf

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -f /etc/xpdfrc ]; then
	echo 'unicodeMap	ISO-8859-7	/usr/X11R6/share/xpdf/ISO-8859-7.unicodeMap' >> /etc/xpdfrc
else
 if ! grep -q /usr/X11R6/share/xpdf/ISO-8859-7.unicodeMap /etc/xpdfrc; then
	echo 'unicodeMap	ISO-8859-7	/usr/X11R6/share/xpdf/ISO-8859-7.unicodeMap' >> /etc/xpdfrc
 fi
fi

%preun
grep -v /usr/X11R6/share/xpdf/ISO-8859-7.unicodeMap /etc/xpdfrc > /etc/xpdfrc.new
mv -f /etc/xpdfrc.new /etc/xpdfrc

%files
%defattr(644,root,root,755)
%doc README add-to-xpdfrc
%{_datadir}/xpdf/*
