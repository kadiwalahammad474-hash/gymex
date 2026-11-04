<?php

// Security: only accept POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    exit('Method not allowed');
}

// Security: sanitize all user input
function sanitize($val) {
    return htmlspecialchars(trim($val ?? ''), ENT_QUOTES, 'UTF-8');
}

// reCAPTCHA verification
$recaptchaSecret = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'; // test secret key
$recaptchaResponse = $_POST['g-recaptcha-response'] ?? '';
if (empty($recaptchaResponse)) {
    echo "<script>alert('Please verify that you are not a robot.'); window.history.back();</script>";
    exit;
}
$verifyUrl = 'https://www.google.com/recaptcha/api/siteverify';
$data = array(
    'secret' => $recaptchaSecret,
    'response' => $recaptchaResponse,
    'remoteip' => $_SERVER['REMOTE_ADDR'] ?? ''
);
$options = array(
    'http' => array(
        'header' => "Content-type: application/x-www-form-urlencoded\r\n",
        'method' => 'POST',
        'content' => http_build_query($data)
    )
);
$context = stream_context_create($options);
$verify = @file_get_contents($verifyUrl, false, $context);
$captchaSuccess = false;
if ($verify !== false) {
    $captchaData = json_decode($verify);
    if ($captchaData && isset($captchaData->success) && $captchaData->success) {
        $captchaSuccess = true;
    }
}
if (!$captchaSuccess) {
    echo "<script>alert('CAPTCHA verification failed. Please try again.'); window.history.back();</script>";
    exit;
}

$firstname  = sanitize($_POST['firstname'] ?? '');
$lastname   = sanitize($_POST['lastname'] ?? '');
$company    = sanitize($_POST['company'] ?? '');
$email      = filter_var(trim($_POST['email'] ?? ''), FILTER_VALIDATE_EMAIL);
$phone      = preg_replace('/[^0-9+\-\s()]/', '', $_POST['phonenumber'] ?? '');
$countrycode = preg_replace('/[^0-9+]/', '', $_POST['countrycode'] ?? '');
$message    = sanitize($_POST['message'] ?? '');

// Get IP Address
function getUserIP() {
    if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
        return $_SERVER['HTTP_CLIENT_IP'];
    } elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
        return explode(',', $_SERVER['HTTP_X_FORWARDED_FOR'])[0];
    } else {
        return $_SERVER['REMOTE_ADDR'] ?? '';
    }
}
$ipAddress = getUserIP();

// Security: validate required fields
if (!$email || !$firstname) {
    http_response_code(400);
    exit('Invalid form data');
}

// Security: whitelist allowed redirect URLs
$allowedHosts = ['gymex.online', 'www.gymex.online', 'localhost'];
$backurl = $_POST['backurl'] ?? 'index.html';
$parsedUrl = parse_url($backurl);
$redirectHost = $parsedUrl['host'] ?? '';
if ($redirectHost && !in_array($redirectHost, $allowedHosts)) {
    $backurl = 'index.html'; // fallback to home
}

require_once('phpmailer/class.phpmailer.php');

$mail = new PHPMailer();
$mail->CharSet = "utf-8";
$mail->IsSMTP();
$mail->SMTPAuth = true;
$mail->Username = "apikey";
// SECURITY: Load API key from environment variable
$mail->Password = getenv('SENDGRID_API_KEY');
if (!$mail->Password) {
    http_response_code(500);
    exit('Email service not configured');
}
$mail->SMTPSecure = "";
$mail->Host = "smtp.sendgrid.net";
$mail->Port = "587";

$mail->setFrom('noreply@gymex.online', 'International Lead');
$mail->AddAddress('support@gymex.online', 'Gymex');

$mail->Subject = 'New Lead From Website';
$mail->IsHTML(true);

$mail->Body  = "There is one new enquiry from website. The details are as below.<br><br>";
$mail->Body .= "<strong>Firstname : </strong>" . $firstname . "<br>";
$mail->Body .= "<strong>Lastname : </strong>" . $lastname . "<br>";
$mail->Body .= "<strong>Company : </strong>" . $company . "<br>";
$mail->Body .= "<strong>Email : </strong>" . $email . "<br>";
$mail->Body .= "<strong>Phone Number : </strong>" . $countrycode . " " . $phone . "<br>";
$mail->Body .= "<strong>Message : </strong>" . $message . "<br>";
$mail->Body .= "<strong>IP Address : </strong>" . $ipAddress . "<br>";

$mail->Send();

?>
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Thank You</title></head>
<body>
<script>
    var url = '<?php echo htmlspecialchars($backurl, ENT_QUOTES, 'UTF-8'); ?>';
    window.location = url + (url.indexOf('?') >= 0 ? '&' : '?') + 'from=email';
</script>
<noscript>
    <meta http-equiv="refresh" content="0;url=<?php echo htmlspecialchars($backurl, ENT_QUOTES, 'UTF-8'); ?>?from=email">
    <p>Redirecting... <a href="<?php echo htmlspecialchars($backurl, ENT_QUOTES, 'UTF-8'); ?>?from=email">Click here</a></p>
</noscript>
</body>
</html>
