'use strict';
{
    const inputTags = ['BUTTON', 'INPUT', 'SELECT', 'TEXTAREA'];
    const modelName = document.getElementById('django-admin-form-add-constants').dataset.modelName;
    if (modelName) {
        const form = document.getElementById(modelName + '_form');
        for (const element of form.elements) {
            // HTMLElement.offsetParent returns null when the element is not
            // rendered.
            if (inputTags.includes(element.tagName) && !element.disabled && element.offsetParent) {
                element.focus();
                break;
            }
        }
    }
}

//Сокрытие блоков
var elements = document.getElementsByClassName('field-groups ');
for (var i = 0; i < elements.length; i++) {
  elements[i].style.display = 'none';
}

var elements = document.getElementsByClassName('field-user_permissions');
for (var i = 0; i < elements.length; i++) {
  elements[i].style.display = 'none';
}

//Изменение текста
var innerDiv = document.getElementById('id_is_superuser_helptext').getElementsByTagName('div')[0];
innerDiv.innerHTML = 'Отметьте, если пользователь может добавлять новые записи, удалять существующие и изменять их.';

var labelElement = document.querySelector('label.vCheckboxLabel[for="id_is_superuser"]');
labelElement.innerHTML = 'Права пользователя';

// Изменения цвета текста
var divElement = document.querySelector('div.form-row.field-password');
var aElement = divElement.querySelector('div.help a');
aElement.setAttribute('style', 'color: red;');