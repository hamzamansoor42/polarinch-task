document.getElementById("fileInput").addEventListener("change", function (event) {
    const file = event.target.files[0];
    if (file) {
        const allowedTypes = ["image/heic", "image/jpeg", "image/png", "application/pdf"];
        if (!allowedTypes.includes(file.type)) {
            alert("Invalid file type! Please upload .heic, .jpeg, .png, or .pdf files.");
            event.target.value = "";
        }
    }
});

document.getElementById("uploadButton").addEventListener("click", async function () {
    const fileInput = document.getElementById("fileInput");
    const file = fileInput.files[0];

    if (!file) {
        document.getElementById("message").textContent = "Please select a file!";
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("http://127.0.0.1:8000/upload", {
            method: "POST",
            body: formData
        });

        if (response.ok) {
            document.getElementById("message").textContent = "File uploaded successfully!";
        } else {
            document.getElementById("message").textContent = "Error uploading file!";
        }
    } catch (error) {
        document.getElementById("message").textContent = "Network error!";
    }
});
