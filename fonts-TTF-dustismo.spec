Summary:	Free True Type fonts by Dustismo
Summary(pl.UTF-8):	Darmowe fonty True Type zrobione przez Dustismo
Name:		fonts-TTF-dustismo
Version:	20041002
Release:	1
License:	GPL v2
Group:		Fonts
Source0:	http://www.dustismo.com/fonts/Domestic_Manners.zip
# Source0-md5:	3f5d0178f3b9f9bbabd697090f89c3b9
Source1:	http://www.dustismo.com/fonts/PenguinAttack.tgz
# Source1-md5:	c17ae1d47f8f90e676dda0855da07fe4
Source2:	http://www.dustismo.com/fonts/Dustismo.tgz
# Source2-md5:	b4176e3c8c9083a0a8afe38e94d6c763
Source3:	http://www.dustismo.com/fonts/El_Abogado_Loco.zip
# Source3-md5:	a76dcaff5af2d92668d7b2f20d44a644
Source4:	http://www.dustismo.com/fonts/Progenisis.zip
# Source4-md5:	57096a1974b4bf33cd1e9beb951e205b
Source5:	http://www.dustismo.com/fonts/flatline.zip
# Source5-md5:	104c2d8783ec7689bdddc0683b9321fd
Source6:	http://www.dustismo.com/fonts/MarkedFool.zip
# Source6-md5:	bf678fc9e281eeb57e62c2fb5223ce2c
Source7:	http://www.dustismo.com/fonts/Junkyard.zip
# Source7-md5:	1285f1274ee1630b60946df8eb894ad9
Source8:	http://www.dustismo.com/fonts/ItWasntMe.zip
# Source8-md5:	f6f2e5b2aaa9f87dbce1b81d7808dcff
Source9:	http://www.dustismo.com/fonts/balker.zip
# Source9-md5:	6faef32e5a6372e2c31a6c16da6a14f5
Source10:	http://www.dustismo.com/fonts/Swift.zip
# Source10-md5:	b588d221c4925c463025d6a493fc814a
Source11:	http://www.dustismo.com/fonts/Wargames.zip
# Source11-md5:	6e2a2583f79b512579587b441a25694f
Source12:	http://www.dustismo.com/fonts/Winks.zip
# Source12-md5:	d0bb2c842b19a563287da590662e7f30
URL:		http://www.dustismo.com/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
This package contains very nice and free fonts TTF.

%description -l pl.UTF-8
Ten pakiet zawiera bardzo ładne i darmowe fonty TTF.

%prep
%setup -q -c -a1 -a2
unzip -o %{SOURCE3}
unzip -o %{SOURCE4}
unzip -o %{SOURCE5}
unzip -o %{SOURCE6}
unzip -o %{SOURCE7}
unzip -o %{SOURCE8}
unzip -o %{SOURCE9}
unzip -o %{SOURCE10}
unzip -o %{SOURCE11}
unzip -o %{SOURCE12}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{ttffontsdir}/*.ttf
