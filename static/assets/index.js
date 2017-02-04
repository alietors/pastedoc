$(document).ready(function(){

    var w = window.innerWidth;
    var h = window.innerHeight;

    tinymce.init({
        selector:'#document',
        height : h
    });

    $('#btnDocumentSave').click(function(){
        var document = tinymce.get('document').getContent();
        var title = $('#title').val();

        $.ajax({
            type: 'post',
            url: '/document',
            data: { tinydata: document, title: title},
            async: false,

            success:function(data){
                window.location = "/document/"+data.id;
            }
        });
    });

});