<!-- ajax 관련 코드 (by.세일) 건들지 말 것  -->
<script>
	$(document).ready(function(){
        $('#orders-box').html('');
        listing();
      });

      function listing() {
        $.ajax({
          type: "GET",
          url: "/",
          data: {},
          success: function(response){
             if (response['result'] == 'success') {
               let orders = response['orders'];
               console.log(orders);
               for (let i = 0; i < orders.length; i++) {
                 make_card(orders[i]['name'],orders[i]['count'],orders[i]['address'],orders[i]['phone'])
               }
             } else {
               alert('기사를 받아오지 못했습니다');
             }
          }
        })
	  }
	  
	  

     
</script>