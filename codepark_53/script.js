const body = document.body

let titulo = document.createElement("h1")
titulo.innerText = "Notebook Asus Vivobook"
titulo.id = "titulo"

body.appendChild(titulo) // Exibe o titulo

let card = document.createElement("div")
card.className = "card"


card.innerHTML = `
<h2>Notebook</h2>
<p>Notebook Asus Vivobook 15 AMD Ryzen 5 8GB - 256GB SSD 15,6” Linux M1502IA-EJ251
</p>

<img src="./img/notebook.png" alt="Notebook">

<p>Preço: <strong>R$ 5.999,00</strong></p>
`

body.appendChild(card)