function tab(el) {
    // Получить список вкладок меню
    var menu=el.parentNode;
    var tabs=menu.getElementsByTagName('li');
    for (var i=0; i<tabs.length; i++) {
        // Вкладка
        var tab=tabs[i];
        // Блок контента

        var content=document.getElementById(tab.id+'_content');
        // Это вкладка на которой кликнули мышкой
        if (tab.id==el.id) {
            // Сделать вкладку активной
            tab.className='tab_active';
            // Показать связанный с ней блок контента
            if (content) {
                content.className='tab_content visible';
            }
        }
        else {
            // Сделать вкладку неактивной
            tab.className='';
            // Скрыть связанный с ней блок контента
            if (content) {
                content.className='tab_content';
            }
        }
    }
}


function notify() {
    $.bootstrapGrowl("You complete the exam!", // Messages
        { // options
            type: "info", // info, success, warning and danger
            ele: "body", // parent container
            offset: {
                from: "top",
                amount: 20
            },
            align: "center", // right, left or center
            width: 400,
            delay: 4000,
            allow_dismiss: true, // add a close button to the message
            stackup_spacing: 10
        });
}