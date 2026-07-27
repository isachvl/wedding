document.addEventListener("DOMContentLoaded", () => {

    const container = document.getElementById("guestsContainer");
    const addBtn = document.getElementById("addGuest");
    const hidden = document.getElementById("id_extra_guests");
    const form = document.querySelector("form");

    const MAX_GUESTS = 5;

    addBtn.addEventListener("click", () => {

        const count = container.querySelectorAll(".guest-row").length;

        if (count >= MAX_GUESTS) {
             
            return;
        }

        const row = document.createElement("div");
        row.className = "guest-row d-flex mt-2";

        const input = document.createElement("input");
        input.type = "text";
        input.className = "form-control guest-input";
        input.placeholder = "ФИО гостя";

        const removeBtn = document.createElement("button");
        removeBtn.type = "button";
        removeBtn.className = "btn btn-danger ms-2";
        removeBtn.innerHTML = "✕";

        removeBtn.onclick = () => {
            row.remove();
        };

        row.appendChild(input);
        row.appendChild(removeBtn);

        container.appendChild(row);

    });

    form.addEventListener("submit", () => {

        const guests = [];

        document.querySelectorAll(".guest-input").forEach(input => {

            if (input.value.trim() !== "") {
                guests.push(input.value.trim());
            }

        });

        hidden.value = guests.join("\n");

    });

});