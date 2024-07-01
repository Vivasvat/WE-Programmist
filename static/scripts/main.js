function Toggle(id_checkbox, id_password){
    let temp = document.getElementById(id_checkbox);
    let password = document.getElementById(id_password);

    if (temp.checked){
        password.type = 'password';
    }
    else{
        password.type = 'text';
    }
}

function Edit(){
    let acc = document.getElementById("account__change");

    acc.style.visibility = "visible";
}

