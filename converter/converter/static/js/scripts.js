document.addEventListener('DOMContentLoaded', (event) => {
  const uploadArea = document.getElementById('upload-area');
  const fileInput = document.getElementById('file-input');
  const fileList = document.getElementById('file-list');

  uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('dragging');
  });

  uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('dragging');
  });

  uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('dragging');
    const files = e.dataTransfer.files;
    handleFiles(files);
  });

  fileInput.addEventListener('change', (e) => {
    const files = e.target.files;
    handleFiles(files);
  });

  function handleFiles(files) {
    fileList.innerHTML = ''; // Clear the list
    for (let file of files) {
      if (file.type === "application/pdf" || file.type === "application/vnd.openxmlformats-officedocument.wordprocessingml.document") {
        const listItem = document.createElement('div');
        listItem.textContent = file.name;
        fileList.appendChild(listItem);
      } else {
        const listItem = document.createElement('div');
        listItem.textContent = `Fichier non accepté: ${file.name}`;
        fileList.appendChild(listItem);
      }
    }
  }
});
