<html>
<head>
	<title>Control the LED's</title>
</head>
<body>

<?php
	//List of LED's and their associated GPIO pin #'s
	$leds = array(
		"red" 		=> 18,
		"yellow" 	=> 23,
		"green"		=> 24,
		"blue"		=> 25,
		"white"		=> 4,
	);

	//change state of GPIO pins if data is passed through $_GET
	if(isset($_GET['pin']) && isset($_GET['state'])) {
		$pin = $_GET['pin'];
		$state = $_GET['state'];
		exec('gpio -g write '.$pin.' '.$state); //use the gpio program to write the new pin state
		header('Location: control-leds.php');
	}
?>
	<table>
<?php
	foreach($leds as $color => $pin) {			//read each color out of the $leds array defined above
		$current_state = exec('gpio -g read '.$pin);	//read out the current state of the pin
		echo "\t<tr>";
		echo '<td>'.$color.'</td>';

		if ($current_state == 1) {			//if the led is currently on, bold "on" and make "off" a hyperlink
			echo '<td><b>on</b></td>';
			echo '<td><a href="control-leds.php?pin='.$pin.'&state=0">off</a></td>';
		} elseif($current_state == 0) {			//if the led is currently off, bold "off" and make "on" a hyperlink
			echo '<td><a href="control-leds.php?pin='.$pin.'&state=1">on</a></td>';
			echo '<td><b>off</b></td>';
		}

		echo "</tr>\n";
	}
?>
	</table>
	<p><a href="index.php">Return to Index</a></p>
</body>
</html>
