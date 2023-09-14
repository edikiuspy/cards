<script>
  let color;
  let count = 0;
  let rand;



  async function getRand() {
    const response = await fetch("./card");
    rand = await response.text();
    await getColor();
    await getCount();
  }

  async function getCount() {
    const response = await fetch("./count");
    count = await response.text();
  }
    async function getColor() {
    const response = await fetch("./color");
    color = await response.text();
    if (color === "green") {
      color = "--MEGA, linear-gradient(180deg, #57C630 0%, #1C6B00 100%)";
    } else if (color === "yellow") {
      color = "--Linear, linear-gradient(180deg, #E0AB44 0%, #B76709 100%)";
    } else if (color === "red") {
      color = "--red, linear-gradient(180deg, #D35151 0%, #9A0000 100%)";
    } else if (color === "black") {
      color = "linear-gradient(180deg, #000 0%, #1D1D1D 100%);";
    }
        console.log(color)
  }
  import { onMount } from "svelte";

  onMount(getRand);
</script>

<style>
  .body {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }

  .container {
    display: flex;
    word-wrap: break-word;
    width: 200px;
    height: 500px;
    padding: 76px 78px 75px 77px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border: 37px solid #FFF;
  }

  h1 {
    -webkit-text-stroke: 3px #000000;
    text-shadow: #000000;
    color: #FFF;
    text-align: center;
    font-family: Inter, serif;
    font-size: 50px;
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

<div class="body">
  <div class="container" style="background: var({color})">
    <h1>{rand}</h1>
  </div>
  <h2>{count}</h2>
  <button on:click={getRand}>Get card</button>
</div>
