; Script generated by the HM NIS Edit Script Wizard.

; HM NIS Edit Wizard helper defines
!define PRODUCT_NAME "冬至迈向新年的礼物"
!define PRODUCT_VERSION "1.2"
!define PRODUCT_PUBLISHER "A Lucky Boy"
!define PRODUCT_WEB_SITE "https://blog.csdn.net/qq_54554848?spm=1000.2115.3001.5343"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\commands.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"
!define PRODUCT_STARTMENU_REGVAL "NSIS:StartMenuDir"

; MUI 1.67 compatible ------
!include "MUI.nsh"

; MUI Settings
!define MUI_ABORTWARNING
!define MUI_ICON "setup.ico"
!define MUI_UNICON "unistall.ico"

; Welcome page
!insertmacro MUI_PAGE_WELCOME
; License page
!define MUI_LICENSEPAGE_CHECKBOX
!insertmacro MUI_PAGE_LICENSE "授权文件.rtf"
; Components page
!insertmacro MUI_PAGE_COMPONENTS
; Directory page
!insertmacro MUI_PAGE_DIRECTORY
; Start menu page
var ICONS_GROUP
!define MUI_STARTMENUPAGE_NODISABLE
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "冬至迈向新年的礼物"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "${PRODUCT_UNINST_ROOT_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${PRODUCT_UNINST_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${PRODUCT_STARTMENU_REGVAL}"
!insertmacro MUI_PAGE_STARTMENU Application $ICONS_GROUP
; Instfiles page
!insertmacro MUI_PAGE_INSTFILES
; Finish page
!define MUI_FINISHPAGE_RUN "$DESKTOP\冬至迈向新年的礼物\main.exe"
!insertmacro MUI_PAGE_FINISH

; Uninstaller pages
!insertmacro MUI_UNPAGE_INSTFILES

; Language files
!insertmacro MUI_LANGUAGE "English"

; MUI end ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "Setup.exe"
InstallDir "$DESKTOP\冬至迈向新年的礼物"
InstallDirRegKey HKLM "${PRODUCT_DIR_REGKEY}" ""
ShowInstDetails show
ShowUnInstDetails show

Section "MainSection" SEC01
  SetOutPath "$DESKTOP\冬至迈向新年的礼物"
  SetOverwrite try
  File "author.txt"
  File "bg.jpg"
  File "bg2.png"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物\build\commands"
  File "build\commands\Analysis-00.toc"
  File "build\commands\base_library.zip"
  File "build\commands\commands.exe.manifest"
  File "build\commands\commands.pkg"
  File "build\commands\EXE-00.toc"
  File "build\commands\PKG-00.toc"
  File "build\commands\PYZ-00.pyz"
  File "build\commands\PYZ-00.toc"
  File "build\commands\Tree-00.toc"
  File "build\commands\Tree-01.toc"
  File "build\commands\Tree-02.toc"
  File "build\commands\warn-commands.txt"
  File "build\commands\xref-commands.html"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物\build\main"
  File "build\main\Analysis-00.toc"
  File "build\main\base_library.zip"
  File "build\main\EXE-00.toc"
  File "build\main\main.exe.manifest"
  File "build\main\main.pkg"
  File "build\main\PKG-00.toc"
  File "build\main\PYZ-00.pyz"
  File "build\main\PYZ-00.toc"
  File "build\main\Tree-00.toc"
  File "build\main\Tree-01.toc"
  File "build\main\Tree-02.toc"
  File "build\main\warn-main.txt"
  File "build\main\xref-main.html"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物"
  File "commands.exe"
  File "commands.py"
  File "core.py"
  File "countingStars.py"
  File "cover.ini"
  File "cover.jpg"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物\dist"
  File "dist\commands.spec"
  File "dist\main.spec"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物"
  File "drawtree.py"
  File "favicon.ico"
  File "image_cope.py"
  File "initialize.ini"
  File "jn.mp3"
  File "main.exe"
  File "main.py"
  File "move_ren.py"
  File "move_stars.py"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物\new_year"
  File "new_year\1643084927594-ckt-抠图.png"
  File "new_year\bfe05ea9ly1fxhbfcdkduj21hc0u011u.jpg"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物\new_year\build\虎虎生威"
  File "new_year\build\虎虎生威\Analysis-00.toc"
  File "new_year\build\虎虎生威\base_library.zip"
  File "new_year\build\虎虎生威\EXE-00.toc"
  File "new_year\build\虎虎生威\PKG-00.toc"
  File "new_year\build\虎虎生威\PYZ-00.pyz"
  File "new_year\build\虎虎生威\PYZ-00.toc"
  File "new_year\build\虎虎生威\Tree-00.toc"
  File "new_year\build\虎虎生威\Tree-01.toc"
  File "new_year\build\虎虎生威\Tree-02.toc"
  File "new_year\build\虎虎生威\warn-虎虎生威.txt"
  File "new_year\build\虎虎生威\xref-虎虎生威.html"
  File "new_year\build\虎虎生威\虎虎生威.exe.manifest"
  File "new_year\build\虎虎生威\虎虎生威.pkg"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物\new_year"
  File "new_year\countingStars.py"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物\new_year\dist"
  File "new_year\dist\虎虎生威.spec"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物\new_year"
  File "new_year\favicon.ico"
  File "new_year\fireworks.py"
  File "new_year\fly.png"
  File "new_year\ggyjn.mp3"
  File "new_year\init - 副本.ini"
  File "new_year\init.ini"
  File "new_year\left.jpg"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物\new_year\picture"
  File "new_year\picture\picture0.jpg"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物\new_year"
  File "new_year\right.jpg"
  File "new_year\Sand - China-1.mp3"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物\new_year\sentence"
  File "new_year\sentence\1643082607697-ckt-抠图.png"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物\new_year"
  File "new_year\STXINGKA.TTF"
  File "new_year\swissek.ttf"
  File "new_year\tiger.png"
  File "new_year\使用说明.txt"
  File "new_year\虎虎生威.exe"
  File "new_year\虎虎生威.py"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物"
  File "on_it.py"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物\picture"
  File "picture\picture0.jpg"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物"
  File "Sand - China-1.mp3"
  File "setup.ico"
  File "snow.jpg"
  File "snow_draw.py"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物\tree"
  File "tree\1.png"
  File "tree\11.png"
  File "tree\2.png"
  File "tree\22.png"
  File "tree\3.png"
  File "tree\33.png"
  File "tree\6.png"
  File "tree\7.png"
  File "tree\ddd.mp3"
  File "tree\sds.jpg"
  SetOutPath "$DESKTOP\冬至迈向新年的礼物"
  File "unistall.ico"
  File "授权文件.rtf"

; Shortcuts
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
  CreateShortCut "$DESKTOP\冬至迈向新年的礼物.lnk" "$DESKTOP\冬至迈向新年的礼物\main.exe"
  !insertmacro MUI_STARTMENU_WRITE_END
SectionEnd

Section -AdditionalIcons
  SetOutPath $INSTDIR
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateDirectory "$SMPROGRAMS\$ICONS_GROUP"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Uninstall.lnk" "$INSTDIR\uninst.exe"
  !insertmacro MUI_STARTMENU_WRITE_END
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$DESKTOP\冬至迈向新年的礼物\commands.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$DESKTOP\冬至迈向新年的礼物\commands.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd

; Section descriptions
!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
  !insertmacro MUI_DESCRIPTION_TEXT ${SEC01} ""
!insertmacro MUI_FUNCTION_DESCRIPTION_END


Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) 已成功地从你的计算机移除。"
FunctionEnd

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "你确实要完全移除 $(^Name) ，其及所有的组件？" IDYES +2
  Abort
FunctionEnd

Section Uninstall
  !insertmacro MUI_STARTMENU_GETFOLDER "Application" $ICONS_GROUP
  Delete "$INSTDIR\${PRODUCT_NAME}.url"
  Delete "$INSTDIR\uninst.exe"
  Delete "$DESKTOP\冬至迈向新年的礼物\授权文件.rtf"
  Delete "$DESKTOP\冬至迈向新年的礼物\unistall.ico"
  Delete "$DESKTOP\冬至迈向新年的礼物\tree\sds.jpg"
  Delete "$DESKTOP\冬至迈向新年的礼物\tree\ddd.mp3"
  Delete "$DESKTOP\冬至迈向新年的礼物\tree\7.png"
  Delete "$DESKTOP\冬至迈向新年的礼物\tree\6.png"
  Delete "$DESKTOP\冬至迈向新年的礼物\tree\33.png"
  Delete "$DESKTOP\冬至迈向新年的礼物\tree\3.png"
  Delete "$DESKTOP\冬至迈向新年的礼物\tree\22.png"
  Delete "$DESKTOP\冬至迈向新年的礼物\tree\2.png"
  Delete "$DESKTOP\冬至迈向新年的礼物\tree\11.png"
  Delete "$DESKTOP\冬至迈向新年的礼物\tree\1.png"
  Delete "$DESKTOP\冬至迈向新年的礼物\snow_draw.py"
  Delete "$DESKTOP\冬至迈向新年的礼物\snow.jpg"
  Delete "$DESKTOP\冬至迈向新年的礼物\setup.ico"
  Delete "$DESKTOP\冬至迈向新年的礼物\Sand - China-1.mp3"
  Delete "$DESKTOP\冬至迈向新年的礼物\picture\picture0.jpg"
  Delete "$DESKTOP\冬至迈向新年的礼物\on_it.py"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\虎虎生威.py"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\虎虎生威.exe"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\使用说明.txt"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\tiger.png"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\swissek.ttf"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\STXINGKA.TTF"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\sentence\1643082607697-ckt-抠图.png"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\Sand - China-1.mp3"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\right.jpg"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\picture\picture0.jpg"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\left.jpg"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\init.ini"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\init - 副本.ini"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\ggyjn.mp3"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\fly.png"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\fireworks.py"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\favicon.ico"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\dist\虎虎生威.spec"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\countingStars.py"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\build\虎虎生威\虎虎生威.pkg"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\build\虎虎生威\虎虎生威.exe.manifest"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\build\虎虎生威\xref-虎虎生威.html"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\build\虎虎生威\warn-虎虎生威.txt"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\build\虎虎生威\Tree-02.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\build\虎虎生威\Tree-01.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\build\虎虎生威\Tree-00.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\build\虎虎生威\PYZ-00.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\build\虎虎生威\PYZ-00.pyz"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\build\虎虎生威\PKG-00.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\build\虎虎生威\EXE-00.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\build\虎虎生威\base_library.zip"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\build\虎虎生威\Analysis-00.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\bfe05ea9ly1fxhbfcdkduj21hc0u011u.jpg"
  Delete "$DESKTOP\冬至迈向新年的礼物\new_year\1643084927594-ckt-抠图.png"
  Delete "$DESKTOP\冬至迈向新年的礼物\move_stars.py"
  Delete "$DESKTOP\冬至迈向新年的礼物\move_ren.py"
  Delete "$DESKTOP\冬至迈向新年的礼物\main.py"
  Delete "$DESKTOP\冬至迈向新年的礼物\main.exe"
  Delete "$DESKTOP\冬至迈向新年的礼物\jn.mp3"
  Delete "$DESKTOP\冬至迈向新年的礼物\initialize.ini"
  Delete "$DESKTOP\冬至迈向新年的礼物\image_cope.py"
  Delete "$DESKTOP\冬至迈向新年的礼物\favicon.ico"
  Delete "$DESKTOP\冬至迈向新年的礼物\drawtree.py"
  Delete "$DESKTOP\冬至迈向新年的礼物\dist\main.spec"
  Delete "$DESKTOP\冬至迈向新年的礼物\dist\commands.spec"
  Delete "$DESKTOP\冬至迈向新年的礼物\cover.jpg"
  Delete "$DESKTOP\冬至迈向新年的礼物\cover.ini"
  Delete "$DESKTOP\冬至迈向新年的礼物\countingStars.py"
  Delete "$DESKTOP\冬至迈向新年的礼物\core.py"
  Delete "$DESKTOP\冬至迈向新年的礼物\commands.py"
  Delete "$DESKTOP\冬至迈向新年的礼物\commands.exe"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\main\xref-main.html"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\main\warn-main.txt"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\main\Tree-02.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\main\Tree-01.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\main\Tree-00.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\main\PYZ-00.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\main\PYZ-00.pyz"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\main\PKG-00.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\main\main.pkg"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\main\main.exe.manifest"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\main\EXE-00.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\main\base_library.zip"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\main\Analysis-00.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\commands\xref-commands.html"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\commands\warn-commands.txt"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\commands\Tree-02.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\commands\Tree-01.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\commands\Tree-00.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\commands\PYZ-00.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\commands\PYZ-00.pyz"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\commands\PKG-00.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\commands\EXE-00.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\commands\commands.pkg"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\commands\commands.exe.manifest"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\commands\base_library.zip"
  Delete "$DESKTOP\冬至迈向新年的礼物\build\commands\Analysis-00.toc"
  Delete "$DESKTOP\冬至迈向新年的礼物\bg2.png"
  Delete "$DESKTOP\冬至迈向新年的礼物\bg.jpg"
  Delete "$DESKTOP\冬至迈向新年的礼物\author.txt"

  Delete "$SMPROGRAMS\$ICONS_GROUP\Uninstall.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Website.lnk"
  Delete "$DESKTOP\冬至迈向新年的礼物.lnk"

  RMDir "$SMPROGRAMS\$ICONS_GROUP"
  RMDir "$DESKTOP\冬至迈向新年的礼物\tree"
  RMDir "$DESKTOP\冬至迈向新年的礼物\picture"
  RMDir "$DESKTOP\冬至迈向新年的礼物\new_year\sentence"
  RMDir "$DESKTOP\冬至迈向新年的礼物\new_year\picture"
  RMDir "$DESKTOP\冬至迈向新年的礼物\new_year\dist"
  RMDir "$DESKTOP\冬至迈向新年的礼物\new_year\build\虎虎生威"
  RMDir "$DESKTOP\冬至迈向新年的礼物\new_year"
  RMDir "$DESKTOP\冬至迈向新年的礼物\dist"
  RMDir "$DESKTOP\冬至迈向新年的礼物\build\main"
  RMDir "$DESKTOP\冬至迈向新年的礼物\build\commands"
  RMDir "$DESKTOP\冬至迈向新年的礼物"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd