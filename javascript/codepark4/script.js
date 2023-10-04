let titulo = document.querySelector("#titulo")

titulo.innerText = 'Titulo'


let link = document.querySelector("a")

link.innerText = 'Link Talento Cloud.'


let lista_ordenada = document.querySelector('#lista-ordenada')


lista_ordenada.innerHTML = `
<p>Lista ordenada.</p>
<li>Item1</li>
<li>Item2</li>
<li>Item3</li>
`

let lista_nao_ordenada = document.querySelector('ul')

lista_nao_ordenada.innerHTML = `
<p>Lista Não ordenada.</p>
<li><a href="https://www.youtube.com/">Link1</a>
<li><a href="https://www.instagram.com/">Link2</a>
<li><a href="https://www.instagram.com/">Link3</a>

`