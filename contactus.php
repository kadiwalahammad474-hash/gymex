<?php


 require_once('phpmailer/class.phpmailer.php');
	
 $mail = new PHPMailer();
    $mail->CharSet =  "utf-8";
    $mail->IsSMTP();
    $mail->SMTPAuth = true;
    $mail->Username = "apikey";
    $mail->Password = "YOUR_SENDGRID_API_KEY_HERE";
	$mail->SMTPSecure = "";  
    $mail->Host = "smtp.sendgrid.net";
    $mail->Port = "587";
 
    $mail->setFrom('noreply@gymex.online', 'Inertnational Lead');
    $mail->AddAddress('support@gymex.online', 'Gymex');

    $mail->Subject  =  'New Lead From Website';
    $mail->IsHTML(true);
            
    $mail->Body .= "There is one new enquiry from website. The details are as below.\r\n<br>\r\n<br>";
	  $mail->Body .= "<strong>Firstname : </strong>".$_POST['firstname']."\r\n<br>"; //mail body
	  $mail->Body .= "<strong>Lastname : </strong>".$_POST['lastname']."\r\n<br>"; //mail body
	  $mail->Body .= "<strong>Company : </strong>".$_POST['company']."\r\n<br>"; //mail body
	  $mail->Body .= "<strong>Email : </strong>".$_POST['email']."\r\n<br>"; //mail body
    $mail->Body .= "<strong>Phone Number : </strong>".$_POST['countrycode']." ".$_POST['phonenumber']."\r\n<br>"; //mail body
	  $mail->Body .= "<strong>Message : </strong>".$_POST['message']."\r\n<br>"; //mail body
		
    if ($mail->Send()) 
	{
	} 
	else 
	{
	}

	 $backurl = $_POST['backurl'];
  
?>


<script> 
	var url = '<?php echo $backurl; ?>';
	window.location = url + "?from=email";
</script>
