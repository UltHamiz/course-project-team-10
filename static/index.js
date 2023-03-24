function switchForm(formType) {
    const incomeForm = document.getElementById("income-form");
    const spendingForm = document.getElementById("spending-form");
    const incomeButton = document.querySelector("button[onclick=\"switchForm('income')\"]");
    const spendingButton = document.querySelector("button[onclick=\"switchForm('spend')\"]");

    if (formType === "income") {
        incomeForm.style.display = "block";
        spendingForm.style.display = "none";
        incomeButton.classList.add("active");
        spendingButton.classList.remove("active");
    } else if (formType === "spend") {
        incomeForm.style.display = "none";
        spendingForm.style.display = "block";
        incomeButton.classList.remove("active");
        spendingButton.classList.add("active");
    }
}



function validateForm(event, form) {
    const inputs = form.querySelectorAll('input[type="text"], input[type="number"], input[type="date"]');

    for (const input of inputs) {
        if (!input.value.trim()) {
            event.preventDefault();
            alert('Please fill in all the fields before submitting the form.');
            return false;
        }
    }

    return true;
}
