<?php
    include_once 'header.php'
?>

<div class="container">
  <div class="row">
    <div class="col-lg-9 col-md-9">
        <?php
          echo "<h1>" . $_SESSION["usersname"] . "'s Account</h1>";
        ?>
    </div>
  </div>
</div>
<div style="height:590px"></div>

<?php
    include_once 'footer.php'
?>