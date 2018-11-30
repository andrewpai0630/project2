var addclass = 'color';
 $(".form-check-input").click(function() {
     if ($(this).hasClass('color')) {
         $(this).removeClass('color');
     }
     else{      
         if($(".color").length < 2) {
            $(this).toggleClass(addclass);
         }
        }
});
$(":submit").click(function(){
var res=[];
$(".form-check-input").each(function(){
if($(this).hasClass('color')){
res.push($(this).attr('id'))
}

})
alert(res)
})

