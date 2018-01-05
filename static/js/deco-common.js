
//顶部搜索栏搜索方法
function search_click(){
    var keywords = $('#search_keywords').val(),
        request_url = '';
    if(keywords == ""){
        return
    }
    if(type == "python_blog"){
        request_url = "/python_blog/?keywords="+keywords
    }else if(type == "teacher"){
        request_url = "/org/teacher/list?keywords="+keywords
    }
    window.location.href = request_url
}



//顶部搜索栏搜索按钮事件
$('#jsSelectOption').on('click', function(){
    var $jsSelectMenu = $('#jsSelectMenu');
    if($jsSelectMenu.css('display') == 'block') return;
    $jsSelectMenu.addClass('dis');
});
$('#jsSelectMenu > li').on('click', function(){
    var searchType = $(this).attr('data-value'),
        searchName = $(this).text(),
        $jsSelectOption = $('#jsSelectOption');
    $jsSelectOption.attr('data-value',searchType).text(searchName);
    $(this).parent().removeClass('dis');
});
$(document).on('click', function(e){
    if(e.target != $('#jsSelectOption')[0] && e.target != $('#jsSelectMenu')[0]){
        $('#jsSelectMenu').removeClass('dis');
    }
});


$('#jsSearchBtn').on('click',function(){
    search_click()
});
//搜索表单键盘事件
$("#search_keywords").keydown(function(event){
    if(event.keyCode == 13){
         $('#jsSearchBtn').trigger('click');
    }
})
