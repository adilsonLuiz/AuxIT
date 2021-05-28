# Antes de executar este scripting, favor executar como administrador o seguinte comando no PW
# Set-ExecutionPolicy Unrestricted
# Global variable
# Author: Ad code

$local_power_user = "User01"
$local_power_user_passwd = "PassStrongHere"



[array]$packager = 'googlechrome', 'firefox','anydesk.install',
		    		'vlc', 'cutepdf', 'dotnet4.5.2',
		   			'7zip', 'winrar', 'foxitreader',
					'k-litecodecpackfull', 'microsoft-teams',
					'anydesk', 'forticlientvpn',
					'office365business', 'fusioninventory-agent.install',
					'wps-office-free','jre8'


function install_choco {
	Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
		
}

function configure_choco {
	choco config set --name commandExecutionTimeoutSeconds --value 14400
	choco config set --name serviceInstallsDefaultUserName --value $local_power_user
	choco config set --name serviceInstallsDefaultUserPassword --value $local_power_user_passwd

}

function setup_config_program {
	$anydesk_password = 'PassForAnydeskHere'

	Write-Output $anydesk_password | anydesk --set-password
}

function install_packager_with_office365 {
	foreach ($program in $packager) {
		if($program -eq 'wps-office-free') { continue }
		choco install $program  --force --force-dependencies -y
	} 

}

function install_packager_with_wps {
	foreach($program in $packager) {
		if($program -eq 'office365business') { continue }
		choco install $program -y --force --force-dependencies
		
	}
}

function put_machine_domain {
	#TODO detectar se maquina é windows ou ou windows pro
	$machine_new_name = Read-Host 'Informe o nome para a maquina'
	$user_domain_admin = 'userDomainAdministratorHere'
	$domain_name = 'domain.net'
	
	Set-DnsClientServerAddress "Ethernet" -ServerAddresses ("8.8.4.4","8.8.8.8")
	Add-Computer -DomainName $domain_name  -NewName $machine_new_name -Credential $domain_name\$user_domain_admin -Restart
}

function delete_old_power_users {
    [array]$users_old = "admin"
    
    foreach($user in $users_old) {
		net user $user /delete
		Clear-Host
	}
}
	
function create_user_new_power_user {

	net user $local_power_user $local_power_user_passwd /add
	net localgroup administradores $local_power_user /add
}


	
function main {

	Clear-Host
	Write-Output 'Adequar maquina' $env:computername
	$install_type = Read-Host 'Com office[1], sem office [2]' 
	$install_type = $install_type -as [int] # Convertendo opção para int type
	
	install_choco # instala o choco
	configure_choco # Instruções de configuração do Choco
	
	if($install_type -eq 1) { install_packager_with_wps }
	else { install_packager_with_office365 }

	delete_old_power_users
	create_user_new_power_user
	put_machine_domain
	setup_config_program

}

# Main program began here


main

