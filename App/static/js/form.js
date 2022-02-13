const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

username.addEventListener("input",check_username);
email.addEventListener("input",check_email);
password.addEventListener("input",check_password);
password2.addEventListener("input",check_confirm_password);
function check_username(e){
    let target=e.target;
    let ele=document.getElementById("umsg")
    if(target.value.trim()===''){
        ele.innerText= 'Username cannot be blank'
	} else {
        
		ele.innerText=""
    }
}
function check_email(e){
   let target=e.target;
   let ele=document.getElementById("emsg")
   if(target.value.trim() === '') {
    ele.innerText="Email cannot be empty"
} else if (!isEmail(target.value.trim())) {
    ele.innerText="Not a valid email"
} else {
    ele.innerText=""

}

}
function check_password(e){
    let target=e.target;
    let ele=document.getElementById("pmsg")
    if(target.value.trim().length<8)
    {
        ele.innerText='Password cannot be less than 8 characters'
        
	}
    else if(target.value.trim()==='')
    {
        ele.innerText='Password cannot be empty'
    } 
    else {
		ele.innerText=""
    }
}
function check_confirm_password(e){
    let target=e.target;
    ele=document.getElementById("cpmsg")
    let passwordValue=password.value.trim();
    if(target.value.trim()!==passwordValue)
    {
        ele.innerText='Passwords does not match';
    }
    else if(target.value.trim()==='')
    {
        ele.innerText='This field cannot be blank';
    }
    else{
        ele.innerText=""
    }
}

// function checkInputs() {
// 	// trim to remove the whitespaces
// 	const usernameValue = username.value.trim();
// 	const emailValue = email.value.trim();
// 	const passwordValue = password.value.trim();
// 	const password2Value = password2.value.trim();
	
// 	if(usernameValue === '') {
// 		setErrorFor(username, 'Username cannot be blank');
// 	} else {
// 		setSuccessFor(username);
// 	}
	
// 	if(emailValue === '') {
// 		setErrorFor(email, 'Email cannot be blank');
// 	} else if (!isEmail(emailValue)) {
// 		setErrorFor(email, 'Not a valid email');
// 	} else {
// 		setSuccessFor(email);
// 	}
	
// 	if(passwordValue === '') {
// 		setErrorFor(password, 'Password cannot be blank');
// 	} else {
// 		setSuccessFor(password);
// 	}
	
// 	if(password2Value === '') {
// 		setErrorFor(password2, 'Password2 cannot be blank');
// 	} else if(passwordValue !== password2Value) {
// 		setErrorFor(password2, 'Passwords does not match');
// 	} else{
// 		setSuccessFor(password2);
// 	}
//}

// function setErrorFor(input, message) {
// 	const formControl = input.parentElement;
// 	const small = formControl.querySelector('small');
// 	formControl.className = 'form-control error';
// 	small.innerText = message;
// }

// function setSuccessFor(input) {
// 	const formControl = input.parentElement;
// 	formControl.className = 'form-control success';
// }
	
function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}