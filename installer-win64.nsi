# SOURCES
# https://blog.kempj.co.uk/2014/10/packaging-python-app-windows/
# https://nsis.sourceforge.io/A_simple_installer_with_start_menu_shortcut_and_uninstaller

!define APPNAME "Calculator"
!define DESCRIPTION "A simple calculator application"
!define VERSIONMAJOR 0
!define VERSIONMINOR 9
!define VERSIONBUILD 3

# These will be displayed by the "Click here for support information" link in "Add/Remove Programs"
# It is possible to use "mailto:" links in here to open the email client
!define HELPURL "https://stephenroille.github.io/Calculator"
!define UPDATEURL "https://pypi.org/project/calculator/"
!define ABOUTURL "https://www.github.com/StephenRoille/calculator"

# Size [kB] of all the files copied into "Program Files"
!define INSTALLSIZE 7233

# custom files to include from PyInstalller distribution
!define FILES_SOURCE_PATH ".pyinstaller\dist\calculator"
!define ICON "calculator\img\pypi.ico"

RequestExecutionLevel admin ;Require admin rights on NT6+ (When UAC is turned on)

InstallDir "$PROGRAMFILES64\${APPNAME}"
LicenseData "LICENSE"
# This will be in the installer/uninstaller's title bar
Name "${APPNAME}"
Icon "${ICON}"
outFile "calculator-installer-x64.exe"

!include LogicLib.nsh

# show 3 pages - license, location, and installation
page license
page directory
Page instfiles

!macro VerifyUserIsAdmin
UserInfo::GetAccountType
pop $0
${If} $0 != "admin" ;Require admin rights on NT4+
        messageBox mb_iconstop "Administrator rights required!"
        setErrorLevel 740 ;ERROR_ELEVATION_REQUIRED
        quit
${EndIf}
!macroend

function .onInit
    setShellVarContext all
    !insertmacro VerifyUserIsAdmin
functionEnd

section "install"
    # Files for the install directory - to build the installer, these should be in the same directory as the install script (this file)
    setOutPath $INSTDIR
    SetRegView 64

    # Files added here should be removed by the uninstaller (see section "uninstall")
    File /r "${FILES_SOURCE_PATH}\*"
    File "README.md"
    File "CodeOfConduct.md"
    File "LICENSE"
    File "${ICON}"

    # Uninstaller - See function un.onInit and section "uninstall" for configuration
    writeUninstaller "$INSTDIR\uninstall.exe"

    # Start Menu
    createDirectory "$SMPROGRAMS\"
    createShortCut "$SMPROGRAMS\${APPNAME}.lnk" "$INSTDIR\calculator.exe" "" "$INSTDIR\pypi.ico"

    # Registry information for add/remove programs
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayName" "${APPNAME} - ${DESCRIPTION}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "UninstallString" "$\"$INSTDIR\uninstall.exe$\""
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "InstallLocation" "$\"$INSTDIR$\""
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayIcon" "$\"$INSTDIR\pypi.ico$\""
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "Readme" "$\"$INSTDIR\README.md$\""
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "HelpLink" ${HELPURL}
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "Publisher" "Stephen Roille"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "URLUpdateInfo" ${UPDATEURL}
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "URLInfoAbout" ${ABOUTURL}
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayVersion" "${VERSIONMAJOR}.${VERSIONMINOR}.${VERSIONBUILD}"
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "VersionMajor" ${VERSIONMAJOR}
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "VersionMinor" ${VERSIONMINOR}
    # There is no option for modifying or repairing the install
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "NoModify" 1
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "NoRepair" 1
    # Set the INSTALLSIZE constant (!defined at the top of this script) so Add/Remove Programs can accurately report the size
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "EstimatedSize" ${INSTALLSIZE}
sectionEnd

# Uninstaller
function un.onInit
    SetShellVarContext all
    SetRegView 64

    #Verify the uninstaller - last chance to back out
    MessageBox MB_OKCANCEL "Permanantly remove the ${APPNAME} app?" IDOK next
        Abort
    next:
    !insertmacro VerifyUserIsAdmin
functionEnd

section "uninstall"
    SetRegView 64

    # Remove Start Menu launcher
    delete "$SMPROGRAMS\${APPNAME}.lnk"
    # Try to remove the Start Menu folder - this will only happen if it is empty
    rmDir "$SMPROGRAMS\"
    # Remove the install directory recursively, files that cannot be removed wil be deleted on reboot
    rmDir /r /REBOOTOK $INSTDIR
    # Remove uninstaller information from the registry
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}"
sectionEnd
