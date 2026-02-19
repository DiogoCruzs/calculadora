; ===========================================================
; Script Inno Setup - Calculadora Python
; Projeto: Segurança e Auditoria de Sistemas (ADS)
; ===========================================================

[Setup]
; Informações do aplicativo
AppName=Calculadora
AppVersion=1.0.0
AppPublisher=Projeto ADS - Segurança e Auditoria
AppPublisherURL=https://github.com/seu-usuario/calculadora
DefaultDirName={autopf}\Calculadora
DefaultGroupName=Calculadora
OutputDir=Output
OutputBaseFilename=CalculadoraSetup
SetupIconFile=
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest

; Compatibilidade
MinVersion=10.0
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible

[Languages]
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "Criar atalho na Área de Trabalho"; GroupDescription: "Atalhos adicionais:"; Flags: unchecked

[Files]
; Executável gerado pelo PyInstaller
Source: "dist\Calculadora.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Atalho no Menu Iniciar
Name: "{group}\Calculadora"; Filename: "{app}\Calculadora.exe"
; Atalho na Área de Trabalho (opcional)
Name: "{autodesktop}\Calculadora"; Filename: "{app}\Calculadora.exe"; Tasks: desktopicon
; Atalho para desinstalar
Name: "{group}\Desinstalar Calculadora"; Filename: "{uninstallexe}"

[Run]
; Abrir o aplicativo após a instalação
Filename: "{app}\Calculadora.exe"; Description: "Abrir Calculadora"; Flags: nowait postinstall skipifsilent
