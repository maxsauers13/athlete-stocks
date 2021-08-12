<?php
  include_once 'header.php'
?>

  <section class="index-intro">
    <?php
      if (isset($_SESSION["useruid"])) {
        echo "<p>Hello there " . $_SESSION["useruid"] . "</p>";
      }
    ?>
    <h1>NBA Trading Desk</h1>
  </section>

  <section class="index-categories">
    <h2>Actions</h2>
    <div class="index-categories-list">
      <div>
        <h3>Buy</h3>
      </div>
      <div>
        <h3>Sell</h3>
      </div>
      <div>
        <h3>Explore</h3>
      </div>
    </div>
  </section>

<?php
  include_once 'footer.php'
?>