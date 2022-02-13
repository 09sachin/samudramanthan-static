const email = document.getElementById('email');
email.addEventListener("input",check_email);
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
function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}