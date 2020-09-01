<?php

public function shopapi($query)
{
    $client_id = "oXfhI4we88tBhBs1hxY_";
    $client_secret = "mruETz2SMm";
    $searchUrl = "	https://openapi.naver.com/v1/search/shop.json"; // 오픈 API 호출 URL
    $addset = urlencode("&display=10&start=1&sort=sim")

    $is_post = false;
    $ch = curl_init();
    $url = sprintf("%s?query=%s%s" , $searchUrl, $query, $addset)
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, $is_post);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
 
    $headers = array();
    $headers[] = "X-Naver-Client-Id: ".$client_id;
    $headers[] = "X-Naver-Client-Secret: ".$client_secret;

    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    $response = curl_exec ($ch);
    $status_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    echo "status_code:".$status_code."
  ";
    curl_close ($ch);
    if($status_code == 200) {
      $result = json_decode($response, true);
    } else {
      echo "Error 내용:".$response;
    }

    return $result

\
?>