<?php
  include_once 'header.php'
?>

  <section class="signup-form">
    <h2>Sign Up</h2>
    <form action="includes/signup.inc.php" method="post">
      <input type="text" name="name" placeholder="Full Name">
      <input type="text" name="email" placeholder="Email">
      <input type="text" name="username" placeholder="Username">
      <input type="text" name="pwd" placeholder="Password">
      <input type="text" name="pwdconfirm" placeholder="Confirm Password">
      <button type="submit" name="submit">Sign Up</button>
    </form>

    <?php
      if (isset($_GET["error"])) {
        if ($_GET["error"] == "emptyinput") {
          echo "<p>Fill in all of the fields.</p>";
        }
        else if ($_GET["error"] == "invaliduid") {
          echo "<p>Your username has invalid characters.</p>";
        }
        else if ($_GET["error"] == "invalidemail") {
          echo "<p>Your email is invalid.</p>";
        }
        else if ($_GET["error"] == "passwordsdontmatch") {
          echo "<p>Your passwords don't match.</p>";
        }
        else if ($_GET["error"] == "stmtfailed") {
          echo "<p>Something went wrong. Try again.</p>";
        }
        else if ($_GET["error"] == "usernametaken") {
          echo "<p>Username already taken.</p>";
        }
        else if ($_GET["error"] == "none") {
          echo "<p>You have signed up!</p>";
        }
      }
    ?>
  </section>

<?php
  include_once 'footer.php'
?>