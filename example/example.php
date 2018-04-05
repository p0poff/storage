<?
function upload($filepath){
	$DOMAIN = 'http://example.com';
	$SECRET_KEY = 'secret_key';
	$PORT = 80;
	if(is_file($filepath)){
		$pathinfo = pathinfo($filepath);
		$realpath = realpath($filepath);
		$url = $DOMAIN.'upload/key/'.$SECRET_KEY;
		if (version_compare(PHP_VERSION, '5.5.0') >= 0) {
			$arData = array('fileToUpload' => new CURLFile($realpath, 'image/'.$pathinfo['extention'], $pathinfo['basename']));
		} else {
			$arData = array('fileToUpload' => '@' . $realpath . ';filename='.$pathinfo['basename']);
		}
		if ($curl = curl_init($url)) {
			curl_setopt($curl, CURLOPT_POST, true);
			curl_setopt($curl, CURLOPT_PORT, $PORT);
			curl_setopt(
				$curl,
				CURLOPT_POSTFIELDS,
				$arData);
			curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
			$response = curl_exec($curl);
			curl_close($curl);
			return $response;
		} else {
			return 'error';
		}
	}else{
		return 'error';
	}
}
echo upload('cat.jpg');