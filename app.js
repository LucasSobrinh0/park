// Selecionando todos os containers
const containers = document.querySelectorAll('.park-container');

// Adicionando evento de clique para cada container
containers.forEach(container => {
    container.addEventListener('click', () => {
        // Verificando se o container está ocupado (vermelho) ou não (verde)
        if (container.classList.contains('occupied')) {
            // Se está ocupado, perguntar se deseja desocupar
            const confirmRelease = confirm("Tem certeza que deseja desocupar esta vaga?");
            if (confirmRelease) {
                container.classList.remove('occupied');
                container.style.backgroundColor = 'rgb(4, 255, 4)';
            }
        } else {
            // Se não está ocupado, perguntar se deseja ocupar
            const confirmOccupy = confirm("Tem certeza que deseja colocar esta vaga como ocupada?");
            if (confirmOccupy) {
                container.classList.add('occupied');
                container.style.backgroundColor = '#ff3838';
            }
        }
    });
});
