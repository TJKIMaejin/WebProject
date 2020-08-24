// ajax 관련 코드 (by.세일) 건들지 말 것 

	$(document).ready(function(){
        $('#orders-box').html('');
        listing();
      });

      function listing() {
        $.ajax({
          type: "GET",
          url: "/orders",
          data: {},
          success: function(response){
             if (response['result'] == 'success') {
               let orders = response['orders'];
               console.log(orders);
               for (let i = 0; i < orders.length; i++) {
                 make_card(orders[i]['name'],orders[i]['category'])
               }
             } else {
               alert('기사를 받아오지 못했습니다');
             }
          }
        })
	  }
	  
	  

     
