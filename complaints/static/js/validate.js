function validateForm() {

    let email = document.querySelector("input[name='email']").value.trim();
    let subject = document.querySelector("input[name='subject']").value.trim();
    let description = document.querySelector("textarea[name='description']").value.trim();

    if (email === "") {
        alert("Please enter your email");
        return false;
    }

    if (subject === "") {
        alert("Please enter subject");
        return false;
    }

    if (description === "") {
        alert("Please describe the issue");
        return false;
    }

    // all good
    return true;
}
