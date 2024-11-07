// scripts.js

document.addEventListener("DOMContentLoaded", function() {
    const createBlockForm = document.getElementById("create-block-form");
    const blockList = document.getElementById("block-list");
    const blockSelectButton = document.getElementById("block-select-button");

    if (createBlockForm) {
        createBlockForm.addEventListener("submit", function(event) {
            const name = document.getElementById("block-name").value;
            const language1 = document.getElementById("language1").value;
            const language2 = document.getElementById("language2").value;

            if (name.length < 2 || name.length > 15 || 
                language1.length < 2 || language1.length > 15 || 
                language2.length < 2 || language2.length > 15) {
                event.preventDefault();
                alert("Alle Felder müssen zwischen 2 und 15 Zeichen lang sein.");
            }
        });
    }

    if (blockSelectButton) {
        blockSelectButton.addEventListener("click", function() {
            blockList.classList.toggle("d-none");
        });
    }
});