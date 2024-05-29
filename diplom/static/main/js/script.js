document.addEventListener("DOMContentLoaded", function() {
    const deleteBtn = document.getElementById("delete-selected-btn");
    const table = document.getElementById("info-table");
    const NameTable = document.getElementById("forms_table").name;
    deleteBtn.addEventListener("click", function(event) {
        event.preventDefault();
        const checkboxes = table.querySelectorAll("input[id='tb_checkbox']:checked");
        const checkboxValues = Array.from(checkboxes).map(function(checkbox) {
            return checkbox.value;
        });
        if (checkboxValues.length === 0) {
            alert('Не выбрано ни одной записи для удаления.');
            return;
        }
        const csrfToken = getCookie("csrftoken");
        if (confirm('Вы уверены, что хотите удалить выбранные записи?')) {
            fetch("/home/delete-records", {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                },
                body: JSON.stringify({
                    checkboxValues: checkboxValues,
                    NameTable: NameTable
                }),
            }).then(response => {
                if (response.ok) {
                    checkboxes.forEach(function(checkbox) {
                        const row = checkbox.closest("tr");
                        row.parentNode.removeChild(row);
                    });
                    alert('Записи успешно удалены.');
                    if (table.querySelectorAll("input[id='th_checkbox']:checked")) {
                        document.getElementById('th_checkbox').checked = this.checked
                    }
                } else {
                    if (NameTable === 'Md') {
                        alert('Произошла ошибка при удалении записей.');
                    } else {
                        alert('Произошла ошибка при удалении записей, возможно это запись уже используется.');
                    }
                }
            });
        }
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('th_checkbox').addEventListener('change', function() {
        const tbCheckboxes = document.getElementsByName('tb_checkbox');
        for (var i = 0; i < tbCheckboxes.length; i++) {
            tbCheckboxes[i].checked = this.checked;
        }
    });
});
document.addEventListener('DOMContentLoaded', function() {
            document.querySelector('#search_index').addEventListener('keyup', function() {
                var searchValue = this.value.toLowerCase();
                var search_id = document.querySelectorAll('#season_name_tr option_name_tr');
                var rows = document.querySelectorAll('#info-table tbody tr');
                var rows_id = document.querySelectorAll('#info-table tbody tr th input');
                for (var i = 0; i < rows.length; i++) {
                    var chapter = rows[i].querySelector('td:nth-child(2)').textContent.toLowerCase();
                    if (chapter.indexOf(searchValue) === -1) {
                        rows[i].style.display = 'none';
                        rows_id[i].id = 'NULL'
                        rows_id[i].name = 'NONE'
                    } else {
                        rows[i].style.display = '';
                        rows_id[i].id = 'tb_checkbox'
                        rows_id[i].name = 'tb_checkbox'
                    }
                }
            });
});
            document.addEventListener('DOMContentLoaded', function() {
                const selectElement = document.querySelector('#season_name_tr');
                var rows = document.querySelectorAll('#info-table tbody tr');
                var match;
                const tableBody = document.querySelector('#info-table tbody')
                var rows_id = document.querySelectorAll('#info-table tbody tr th input');
                document.querySelector('#search-index').addEventListener('keyup', function() {
                    var searchValue = this.value.toLowerCase();
                    const selectedColumn = selectElement.value;
                    Array.from(tableBody.rows).forEach((row) => {
                        const cells = row.cells;
                        switch (selectedColumn) {
                            case 'Раздел':
                                match = 2;
                                break;
                            case 'Подразделение':
                                match = 3;
                                break;
                            case 'Ответственный':
                                match = 4;
                                break;
                            case 'Статус':
                                match = 8;
                                break;
                            case 'Решение':
                                match = 6;
                                break;
                            default:
                                match = -1;
                        }
                        for (var i = 0; i < rows.length; i++) {
                            var chapter = rows[i].querySelector('td:nth-child(' + match + ')').textContent.toLowerCase();
                            if (chapter.indexOf(searchValue) === -1) {
                                rows[i].style.display = 'none';
                                rows_id[i].id = 'NULL'
                                rows_id[i].name = 'NONE'
                            } else {
                                rows[i].style.display = '';
                                rows_id[i].id = 'tb_checkbox'
                                rows_id[i].name = 'tb_checkbox'
                            }
                        }
                    });
                });
            });