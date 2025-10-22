// script.js - adiciona alguns produtos de exemplo e renderiza cards Bootstrap
const produtos = [
  { id: 1, nome: "Fone Bluetooth X", preco: "R$ 199,90", descricao: "Fone sem fio com ótima bateria." },
  { id: 2, nome: "Smartwatch Pro", preco: "R$ 499,00", descricao: "Monitoramento de saúde e notificações." },
  { id: 3, nome: "Teclado Mecânico", preco: "R$ 349,00", descricao: "Switches táteis e iluminação RGB." }
];

function renderProdutos() {
  const container = document.getElementById("produtos");
  if (!container) return;
  container.innerHTML = "";
  produtos.forEach(p => {
    const col = document.createElement("div");
    col.className = "col-md-4";
    col.innerHTML = `
      <div class="card mb-3">
        <div class="card-body">
          <h5 class="card-title">${p.nome}</h5>
          <p class="card-text">${p.descricao}</p>
          <p class="card-text"><strong>${p.preco}</strong></p>
          <a href="#" class="btn btn-primary">Comprar</a>
        </div>
      </div>
    `;
    container.appendChild(col);
  });
}

document.addEventListener("DOMContentLoaded", renderProdutos);
