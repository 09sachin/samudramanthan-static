const rtoggle=document.getElementsByClassName("rtoggle")[0]
const rlinks=document.getElementsByClassName("rnav-links")[0]
const rclick=document.getElementById("rclick")
rtoggle.addEventListener("click",()=>{
    if (rclick.checked)
    rclick.checked=false
    else
    rclick.checked=true
})