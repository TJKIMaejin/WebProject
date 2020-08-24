// ajax 관련 코드 (by.세일) 건들지 말 것 

$(document).ready(function () {

  listing();
  catListing();
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


function catListing(Val) {

  let temp_html = ''
  let gus = []

  if (Val == '알류') {
    gus = ["계란", "달걀", "메추리알", "날치알", "거위알"]

  } else if (Val == '유제품') {
    gus = ["우유", "연유", "버터", "치즈"]
  } else if (Val == '유지류') {
    gus = []
  } else if (Val == '견과류') {
    gus = []
  } else if (Val == '과일류') {
    gus = ["과일","건크랜베리","크랜베리","건포도","포도"]
  } else if (Val == '육류') {
    gus = ["고기","차돌박이"]
  } else if (Val == '콩류') {
    gus = ["검은콩","견과류",]
  } else if (Val == '곡류') {
    gus = []
  } else if (Val == '해조류') {
    gus = ["다시마","건다시마","다시마육수", ]
  } else if (Val == '어패류') {
    gus = ["가자미","갈치","고등어","고등어통조림","참치","참치캔","고추참치",]
  } else if (Val == '갑각류') {
    gus = ["냉동새우","건새우","새우","오징어","갑오징어","게살"]
  } else if (Val == '버섯류') {
    gus = ["팽이버섯"]
  } else if (Val == '채소류') {
    gus = ["깻잎", "숙주나물", "다진마늘", "마늘", "다진생강", "청양고추", "콩나물", "대파", "양파", "고수","가지"
  ,"감자","감자전분","건고추","고추","청양고추","건표고버섯","표고버섯","고구마","고구마줄기"]
  } else if (Val == '소스류') {
    gus = ["간장", "진간장", "국간장", "감식초", "마요네즈", "깨소금", "꿀", "녹말가루", "고춧가루", "들깨가루", "설탕", "소금", "된장", "쌈장", "고추장",
      "구운소금", "굵은고추가루", "굵은소금", "굴소스", "들기름", "참기름", "고기육수", "맛간장", "맛소금", "맛술", "매실액", "매운고추가루",
      "멸치가루", "멸치다시육수", "멸치액젓", "무염버터", "물엿", "바질", "볶은참깨", "새우젓", "사과식초", "시나몬파우더", "식용유", "액젓",
      "깨","올리고당", "올리브유", "짜장가루", "쯔유", "참치액젓", "초고추장", "케첩", "머스타드", "포도씨유", "핫소스", "허브솔트", "후추", "흑설탕",
      "고추냉이",]
  } else if (Val == '기타') {
    gus = ["가래떡","가쓰오부시","강력쌀가루","게맛살","계피","곤약","골뱅이"]

    for (let i = 0; i < gus.length; i++) {
      temp_html += '<option value=' + gus[i] + '>' + gus[i] + '</option>'
    }


    $('#inputState_select2').empty()
    $('#inputState_select2').append(temp_html)

  }