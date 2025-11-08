let number = 0
const countElement= document.getElementById("count")
const incrementButton= document.getElementById("increment")

incrementButton.addEventListener("click",()=>{
    number++
    countElement.textContent=number
})


const Greeting=document.getElementById(("greeting"))
const btn=document.getElementById("btn")

btn.addEventListener("click",()=>{
    Greeting.textContent="Hello my friend!"

})

let logins = []

function renderLogins() {
    const list = document.getElementById("nameinput")
    const counter = document.getElementById("btn")

    list.innerHTML = ""



    for (let i = 0; i < logins.length; i++) {
        list.innerHTML += `
        <li>
        ${i + 1} - ${logins[i]}
        </li>
        `
    }

    counter.innerText = `${logins.length} login${logins.length === 1 ? "" : "s"}`
}

function addLogin() {
    const input = document.getElementById("nameinput")
    const login = input.value.trim()

    if (login === "") {
        alert("Enter a name!")
        return
    }

    logins.push(login) 
    input.value = "" 
    renderLogins()
}


document.getElementById("btn").addEventListener("click", addLogin)
