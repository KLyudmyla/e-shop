$(document).ready(function(){
 $('.support_title1').click(function(){
  $(this).parent().children('div.content').slideToggle(1000);
  return false;
 });
});
