
function create_user {
	$power_user = "userCreateHere"
	$passwd = "StrongPassHere"
	net user $power_user $passwd /add
	net localgroup administradores $power_user /add
}


function delete_old_power_users {
    [array]$users_old = "admin"

    for($count = 0; $count -le $users_old.Count; $count++) {
        net user $users_old[$count] /delete
    }

}

create_user
delete_old_power_users