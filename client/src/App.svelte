<script>
  let rand = -1;

  async function getRand() {
    const response = await fetch("./rand");
    rand = await response.text();
  }
</script>

<style>
    
  .container {
    display: flex;
    width: 200px;
    height: 425px;
    padding: 76px 78px 75px 77px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
      border: 37px solid #FFF;
    background: var(--MEGA, linear-gradient(180deg, #57C630 0%, #1C6B00 100%));

  }

  h1 {
      -webkit-text-stroke: 3px #000000;
      text-shadow: #000000;
      color: #FFF;
    text-align: center;
    font-family: Inter;
    font-size: 64px;
    font-style: italic;
    font-weight: 900;
    line-height: normal;
  }

  button {
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    cursor: pointer;
  }

  button:hover {
    background-color: #0056b3;
  }
</style>

<div class="container">
  <h1>Your number is {rand}!</h1>
  <button on:click={getRand}>Get a random number</button>
</div>