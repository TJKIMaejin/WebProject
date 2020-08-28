// ajax 관련 코드 (by.세일) 건들지 말 것 >>
/* $(document).ready(function () {

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
} */
// ajax 관련 코드 (by.세일) 건들지 말 것 <<



function check(){
  
}

// 체크된 리스트 반환하는 함수: 제출하기 버튼 누르면 실행됨
function getChecked() {
  let checkedlist = []
  
   $(document).ready(function () {
    var el1 = document.getElementsByName("recipe") // name이 recipe인 요소 리스트로 받기
    for (var i in el1) {
      if ($(el1[i]).prop("checked") == true) { // 체크된 항목인 경우 
        // $(checkedlist).append(el1[i].value)
        checkedlist = append(el1[i].value)
        console.log(checkedlist)
      }
    }
  }); 
  //console.log(checkedlist[0])
  return checkedlist;
}

function catListing(Val) {

  let temp_html = ''
  let gus = []

  let select = []

  if (Val == '알류') {
    gus = ["계란", "달걀", "메추리알", "날치알", "거위알"]

    for (let i = 0; i < gus.length; i++) {
      temp_html += '<input type="checkbox" name="recipe" value="' +gus[i]+'" >'+ gus[i]
    }
    
    
    $('#b1').empty()
    $('#b1').append(temp_html)

  } if (Val == '유제품') {
    gus = ["우유", "연유", "버터", "치즈", "모짜렐라치즈", "바나나우유", "바나나아이스크림", "분유", "스트링치즈", "요거트", "요구르트", "우유", "체다치즈", "크림치즈",
      "탈지분유", "파마산치즈", "파마산치즈가루"]


    for (let i = 0; i < gus.length; i++) {
      if (i % 10 == 0) {
        temp_html += '<div></div>'
      }
      temp_html += '<input type="checkbox" name="recipe" value="' +gus[i]+'" >'+ gus[i]

    }

    $('#b2').empty()
    $('#b2').append(temp_html)


  } if (Val == '유지류') {
    gus = ["코코넛오일", "콩기름", "튀김기름"]
    for (let i = 0; i < gus.length; i++) {
      temp_html += '<input type="checkbox" name="recipe" value="' +gus[i]+'" >'+ gus[i]
    }

    $('#b3').empty()
    $('#b3').append(temp_html)
  } if (Val == '견과류') {
    gus = ["아몬드", "아몬드가루", "잣", "캐슈넛", "피칸", "호두"]
    for (let i = 0; i < gus.length; i++) {
      temp_html += '<input type="checkbox" name="recipe" value="' +gus[i]+'" >'+ gus[i]

    }

    $('#b4').empty()
    $('#b4').append(temp_html)
  } if (Val == '과일류') {
    gus = ["과일", "건크랜베리", "크랜베리", "건포도", "포도", "귤", "딸기", "냉동딸기", "딸기잼", "냉동블루베리", "블루베리", "레몬",
      "레몬제스트", "레몬즙", "매실", "바나나", "배", "배즙", "복숭아", "사과", "사과즙", "아보카도", "오렌지", "체리", "크랜베리", "키위", "통조림파인애플",
      "파인애플"
    ]

    for (let i = 0; i < gus.length; i++) {
      if (i % 10 == 0) {
        temp_html += '<div></div>'
      }
      temp_html += '<input type="checkbox" name="recipe" value="' +gus[i]+'" >'+ gus[i]
    }

    $('#b5').empty()
    $('#b5').append(temp_html)
  } if (Val == '육류') {
    gus = ["고기", "차돌박이", "닭", "닭가슴살", "닭날개", "닭다리", "닭똥집", "닭봉", "닭안심", "대패삼겹살", "돈가스",
      "돼지갈비", "돼지고기", "돼지고기간것", "돼지고기불고기용", "돼지고기잡채용", "돼지고기찌개용", "돼지등뼈", "돼지등심", "돼지목살",
      "돼지안심", "돼지앞다리살", "베이컨", "부채살", "비엔나소시지", "삼겹살", "소갈비", "소고기", "소고기간것", "소고기국거리", "소고기다진것", "소고기등심",
      "소고기불고기용", "소고기샤브샤브용", "소고기안심", "소세지", "슬라이스햄", "양지", "차돌박이", "채끝살", "치킨", "치킨너겟", "치킨텐더",
      "프랑크소시지", "항정살", "햄", "훈제닭가슴살", "훈제오리"
    ]

    for (let i = 0; i < gus.length; i++) {
      if (i % 8 == 0) {
        temp_html += '<div></div>'
      }
      temp_html += '<input type="checkbox" name="recipe" value="' +gus[i]+'" >'+ gus[i]

    }

    $('#b6').empty()
    $('#b6').append(temp_html)
  } if (Val == '콩류') {
    gus = ["검은콩", "견과류", "두부", "두유", "땅콩", "땅콩가루", "땅콩버터", "볶은땅콩", "연두부", "완두콩", "콩가루", "팥"]

    for (let i = 0; i < gus.length; i++) {
      if (i % 10 == 0) {
        temp_html += '<div></div>'
      }
      temp_html += '<input type="checkbox" name="recipe" value="' +gus[i]+'" >'+ gus[i]
    }

    $('#b7').empty()
    $('#b7').append(temp_html)
  } if (Val == '곡류') {
    gus = ["박력쌀가루", "쌀", "쌀가루", "오트밀", "옥수수", "옥수수가루", "옥수수통조림",
      "찹쌀", "찹쌀가루", "캔옥수수", "통밀가루"
    ]

    for (let i = 0; i < gus.length; i++) {
      if (i % 10 == 0) {
        temp_html += '<div></div>'
      }
      temp_html += '<input type="checkbox" name="recipe" value="' +gus[i]+'" >'+ gus[i]

    }

    $('#b8').empty()
    $('#b8').append(temp_html)
  } if (Val == '해조류') {
    gus = ["다시마", "건다시마", "다시마육수", "김", "김가루", "김밥김", "김자반", "메생이", "미역", "조미김", "톳", "파래"]

    for (let i = 0; i < gus.length; i++) {
      if ((i + 1) % 12 == 0) {
        temp_html += '<div></div>'
      }
      temp_html += '<input type="checkbox" name="recipe" value="' +gus[i]+'" >'+ gus[i]
    }

    $('#b9').empty()
    $('#b9').append(temp_html)
  } if (Val == '어패류') {
    gus = ["가자미", "갈치", "고등어", "고등어통조림", "참치", "참치캔", "고추참치", "꽁치", "꽁치통조림", "낙지", "문어", "동태", "멸치",
      "명란", "명란젓", "모시조개", "삼치", "바지락", "연어", "연어캔", "잔멸치", "장어", "조기", "중멸치", "지리멸치",
      "참치통조림", "코다리", "홍합", "황태", "황태채", "황태포", "훈제연어"
    ]
    for (let i = 0; i < gus.length; i++) {
      if (i % 10 == 0) {
        temp_html += '<div></div>'
      }
      temp_html += '<input type="checkbox" name="recipe" value="' +gus[i]+'" >'+ gus[i]
    }

    $('#b10').empty()
    $('#b10').append(temp_html)
  } if (Val == '갑각류') {
    gus = ["냉동새우", "보리새우", "건새우", "새우", "대하", "오징어", "갑오징어", "물오징어", "게살", "관자", "꼬막", "꽃게",
      "자숙새우", "칵테일새우", "크래미", "흰다리새우"
    ]
    for (let i = 0; i < gus.length; i++) {
      if (i % 10 == 0) {
        temp_html += '<div></div>'
      }
      temp_html += '<input type="checkbox" name="recipe" value="' +gus[i]+'" >'+ gus[i]
    }

    $('#b11').empty()
    $('#b11').append(temp_html)
  } if (Val == '버섯류') {
    gus = ["팽이버섯", "목이버섯", "만가닥버섯", "맛타리버섯", "건표고버섯", "표고버섯", "백만송이버섯", "버섯", "새송이버섯",
      "애느타리버섯", "양송이버섯", "팽이버섯", "표고버섯", "표고버섯가루"
    ]
    for (let i = 0; i < gus.length; i++) {
      if (i % 9 == 0) {
        temp_html += '<div></div>'
      }
      temp_html += '<input type="checkbox" name="recipe" value="' +gus[i]+'" >'+ gus[i]

    }

    $('#b12').empty()
    $('#b12').append(temp_html)
  } if (Val == '채소류') {
    gus = ["깻잎", "숙주나물", "다진마늘", "다진생강", "청양고추", "콩나물", "비름나물", "대파", "양파", "고수", "가지", "감자", "감자전분", "건고추", "고추", "청양고추", "고구마", "고구마줄기", "김치", "냉이", "꽈리고추", "브로콜리",
      "느타리버섯", "단무지", "단호박", "달래", "당근", "대추", "대파", "더덕", "도라지", "도토리묵", "돌나물", "돌미나리", "돼지호박",
      "두릅", "로메인", "로즈마리", "마늘", "마늘종", "무", "무말랭이", "무순", "미나리", "밤", "방울양배추", "방울토마토", "방풍나물",
      "배추", "부추", "상추", "새싹채소", "샐러드채소", "샐러리", "생강", "생강즙", "생강청", "세발나물", "숙주", "시금치", "시래기", "신김치", "실고추",
      "쌈무", "쌈채소", "쑥갓", "아스파라거스", "아욱", "알배기배추",
      "애호박", "양배추", "양상추", "양파", "얼갈이배추", "연근",
      "열무", "열무김치", "오이", "오이고추", "오이피클", "우거지",
      "우엉", "적양배추", "적채", "조선호박", "쥐똥고추", "쥬키니호박",
      "쪽파", "참나물", "채소", "청경채", "청양고추", "취나물", "치커리",
      "케일", "콩나물", "토마토", "파", "파프리카", "피망", "호박"
    ]
    for (let i = 0; i < gus.length; i++) {
      if (i % 10 == 0) {
        temp_html += '<div></div>'
      }
      temp_html += '<input type="checkbox" name="recipe" value="' +gus[i]+'" >'+ gus[i]
    }

    $('#b13').empty()
    $('#b13').append(temp_html)
  } if (Val == '소스류') {
    gus = ["간장", "진간장", "국간장", "감식초", "마요네즈", "깨소금", "꿀", "녹말가루", "고춧가루", "들깨가루", "설탕", "소금", "된장", "쌈장", "고추장",
      "구운소금", "굵은고추가루", "굵은소금", "굴소스", "들기름", "참기름", "고기육수", "맛간장", "맛소금", "맛술", "매실액", "매운고추가루",
      "멸치가루", "멸치다시육수", "멸치액젓", "무염버터", "물엿", "바질", "볶은참깨", "새우젓", "사과식초", "시나몬파우더", "식용유", "액젓",
      "깨", "올리고당", "올리브유", "짜장가루", "쯔유", "참치액젓", "초고추장", "케첩", "머스타드", "포도씨유", "핫소스", "허브솔트", "후추", "흑설탕",
      "고추냉이", "녹차가루", "누텔라", "데리야끼소스", "돈가스소스", "두반장", "말차가루", "메밀가루", "메이플시럽", "미숫가루", "미향", "쇠고기다시다", "시럽",
      "씨겨자", "아가베시럽", "연겨자", "오레가노", "우스터소스", "원당",
      "월계수잎", "유기농설탕", "초코시럽", "춘장", "칠리소스", "카레",
      "타임", "토마토소스", "토마토케첩", "통후추", "파슬리", "파슬리가루",
      "페퍼론치노", "풋고추", "피시소스", "허니머스터드", "홀그레인머스터드",
    ]
    for (let i = 0; i < gus.length; i++) {
      if (i % 10 == 0) {
        temp_html += '<div></div>'
      }
      temp_html += '<input type="checkbox" name="recipe" value="' +gus[i]+'" >'+ gus[i]

    }

    $('#b14').empty()
    $('#b14').append(temp_html)
  } if (Val == '기타') {
    gus = ["가래떡", "가쓰오부시", "강력쌀가루", "게맛살", "계피", "곤약", "골뱅이", "꽃빵", "누룽지", "모닝빵", "명엽채",
      "당면", "떡", "떡국떡", "또띠야", "라면", "라이스페이퍼", "레드와인", "마카다미아", "마카로니", "만두", "밀가루", "밀가루강력분", "밀가루박력분", "밀가루중력분", "밀떡",
      "바게트", "부침가루", "북어채", "사이다", "생크림", "소면", "소주", "순대", "순두부", "술", "스위트칠리소스", "스테이크소스", "스파게티면", "식빵",
      "쌀국수", "쌀떡볶이떡", "쌀뜨물", "쑥가루", "아이스크림", "어묵",
      "오레오", "오미자청", "올리브", "우동", "유부", "유자청", "이스트",
      "인삼", "전분", "정종", "젤라틴", "오징어", "오징어채", "주꾸미", "쥐포",
      "진미오징어채", "쫄면", "초코칩", "초코펜", "초콜릿", "칼국수", "커피가루",
      "코코넛가루", "코코아가루", "콜라", "크래커", "토마토퓨레", "통깨", "튀김가루",
      "푸실리", "한천가루", "핫케이크가루", "해물믹스", "해바라기씨", "호떡믹스", "호박씨",
      "호박잎", "화이트와인", "화이트초콜릿", "후리가케", "흑임자"
    ]
    for (let i = 0; i < gus.length; i++) {
      if (i % 10 == 0) {
        temp_html += '<div></div>'
      }
      temp_html += '<input type="checkbox" name="recipe" value="' +gus[i]+'" >'+ gus[i]

    }

    $('#b15').empty()
    $('#b15').append(temp_html)
  }



}


