function Toggle(id_checkbox, id_password){
    let temp = document.getElementById(id_checkbox);
    let password = document.getElementById(id_password);

    if (temp.checked){
        password.type = 'password';
    }
    else{
        password.type = 'text';
    }
}

function Edit(){
    let acc = document.getElementById("account__change");

    acc.style.visibility = "visible";
    
}

document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("filter-form");
    const areaInput = document.getElementById("area-input");
    const labels = document.querySelectorAll('.filter-checkbox');

    // Click handler for radio button categories
    labels.forEach(function(label) {
        label.addEventListener("click", function() {
            const radioValue = this.getAttribute('data-value');
            areaInput.value = radioValue;
            form.submit();

            // Delete class 'selected'
            labels.forEach(function(lbl) {
                lbl.classList.remove('selected');
            });

            // Add class 'selected' to the selected item
            this.classList.add('selected');
        });
    });

    // Handler for games dropdown list
    document.getElementById("game-filter").addEventListener("change", function() {
        form.submit();
    });

    // Mark the selected category when loading the page, if it is selected
    const selectedCategory = document.querySelector('.filter-checkbox[data-value="' + areaInput.value + '"]');
    if (selectedCategory) {
        selectedCategory.classList.add('selected');
    }
});