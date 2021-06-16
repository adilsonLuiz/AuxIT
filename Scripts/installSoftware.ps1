# Antes de executar este scripting, favor executar como administrador o seguinte comando no PW
# Set-ExecutionPolicy Unrestricted
# Global variable
# Author: Ad code

# Local Machine 
$local_power_user = "User01"
$local_power_user_passwd = "PassStrongHere"

# Domain administrator variables
$user_domain_admin = 'userDomainAdministratorHere'
$domain_name = 'domain.net'

# add prograns to install with choco
[array]$packager = 'googlechrome', "anydesk.install"


function install_choco {
	Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
		
}

function configure_choco {
	choco config set --name commandExecutionTimeoutSeconds --value 14400
	choco config set --name serviceInstallsDefaultUserName --value $local_power_user
	choco config set --name serviceInstallsDefaultUserPassword --value $local_power_user_passwd

}

function set_configurate_anydesk {
	$anydesk_password = 'PassForAnydeskHere'

	Write-Output $anydesk_password | anydesk --set-password
}


function install_program {
	foreach($program in $packager) {
		choco install $program -y --force --force-dependencies
		
	}
}

function put_machine_domain {
	#TODO detectar se maquina é windows ou ou windows pro
	$machine_new_name = Read-Host 'Informe o nome para a maquina'

	
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
	
function create_power_user {
	net user $local_power_user $local_power_user_passwd /add
	net localgroup administradores $local_power_user /add
}


	
function main {

	Clear-Host
	Write-Output 'Adequar maquina' $env:computername
	
	install_choco # instala o choco
	configure_choco # Instruções de configuração do Choco
	delete_old_power_users
	create_power_user
	install_program
	put_machine_domain
	set_configurate_anydesk

}

# Main program began here


main

