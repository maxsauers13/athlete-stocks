<?php
  session_start();
?>

<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>NBA Trading Desk</title>
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/reset.css">
  </head>
  <body>

    <nav>
      <div class="wrapper">
        <a href="index.php"></a>
        <ul>
          <li><a href="index.php">Home</a></li>
          <?php
            if (isset($_SESSION["useruid"])) {
              echo "<li><a href='account.php'>Account</a></li>";
              echo "<li><a href='includes/logout.inc.php'>Logout</a></li>";
            } else {
              echo "<li><a href='signup.php'>Sign Up</a></li>";
              echo "<li><a href='login.php'>Log In</a></li>";
            }
          ?>
        </ul>
      </div>
    </nav>

<div class="wrapper">