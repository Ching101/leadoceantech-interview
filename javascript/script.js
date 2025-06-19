document.addEventListener("DOMContentLoaded", () => {
  // DOM Elements
  const studentTable = document.getElementById("studentTableBody");
  const addStudentBtn = document.getElementById("addStudentBtn");
  const modal = document.getElementById("studentModal");
  const closeBtn = document.querySelector(".close");
  const studentForm = document.getElementById("studentForm");
  const modalTitle = document.getElementById("modalTitle");
  const searchInput = document.getElementById("searchInput");

  // Student data array
  let students = [
    { id: 1, name: "Mary Jane", grade: "A" },
    { id: 2, name: "Ethan Hunt", grade: "B+" },
    { id: 3, name: "Snoop Dogg", grade: "A-" },
  ];

  // Render the student table
  function renderStudentTable(data = students) {
    studentTable.innerHTML = "";
    data.forEach((student, index) => {
      const row = document.createElement("tr");
      row.innerHTML = `
                <td>${student.id}</td>
                <td>${student.name}</td>
                <td>${student.grade}</td>
                <td>
                    <!-- TODO: Implement Edit functionality -->
                    <button class="action-btn edit-btn" data-id="${student.id}">Edit</button>
                    <button class="action-btn delete-btn" data-id="${student.id}">Delete</button>
                </td>
            `;
      studentTable.appendChild(row);
    });

    // Add event listeners to the delete buttons
    document.querySelectorAll(".delete-btn").forEach((btn) => {
      btn.addEventListener("click", handleDeleteClick);
    });
  }

  // TODO: Implement Add Student functionality
  // TODO: Implement Edit Student functionality

  // Handle Delete button click
  function handleDeleteClick(event) {
    const id = parseInt(event.target.getAttribute("data-id"));
    if (confirm("Are you sure you want to delete this student?")) {
      students = students.filter((student) => student.id !== id);
      renderStudentTable();
    }
  }

  // Handle form submission for adding/editing student
  function handleFormSubmit(event) {
    event.preventDefault();

    // TODO: Get form values
    const name = document.getElementById("studentName").value;
    const grade = document.getElementById("grade").value;

    // TODO: Add or edit student logic
    // TODO: Close modal
    // TODO: Refresh table
  }

  // Filter students based on search input
  function filterStudents() {
    const searchTerm = searchInput.value.toLowerCase();
    if (searchTerm.trim() === "") {
      renderStudentTable();
    } else {
      const filtered = students.filter(
        (student) =>
          student.name.toLowerCase().includes(searchTerm) ||
          student.grade.toLowerCase().includes(searchTerm)
      );
      renderStudentTable(filtered);
    }
  }

  // Event listeners
  addStudentBtn.addEventListener("click", () => {
    // TODO: Implement Add Student functionality
  });

  closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
  });

  window.addEventListener("click", (event) => {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  });

  studentForm.addEventListener("submit", handleFormSubmit);

  searchInput.addEventListener("input", filterStudents);

  // Initial render
  renderStudentTable();
});
