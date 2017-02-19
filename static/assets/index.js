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
        var readonly = $("#js-readonly").is(':checked');

        $.ajax({
            type: 'post',
            url: '/document',
            data: { tinydata: document, title: title, readonly: readonly},
            async: false,

            success:function(data){
                window.location = "/document/"+data.id;
            }
        });
    });

    $('#btnDocumentUpdate').click(function(){
        var document = tinymce.get('document').getContent();
        var title = $('#title').val();
        var readonly = $("#js-readonly").is(':checked');

        $.ajax({
            type: 'put',
            url: '/document',
            data: { tinydata: document, title: title, readonly: readonly},
            async: false,

            success:function(data){
                window.location = "/document/"+data.id;
            }
        });
    });

});