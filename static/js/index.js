// ajax 관련 코드 (by.세일) 건들지 말 것 

$(document).ready(function () {

  listing();
});

function listing() {
  $.ajax({
    type: "GET",
    url: "/orders",
    data: {},
    success: function (response) {
      if (response['result'] == 'success') {
        let orders = response['recipe3'];
        let orders2 = response['recipe'];

        console.log(response);


      } else {
        alert('기사를 받아오지 못했습니다');
      }
    }
  })


}
