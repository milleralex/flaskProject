<script>
    function pressButton(e){
        fetch('http://localhost:5000/btn/' + e.target.id)
        console.log(e.target.id)
        return true
    }
</script>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');

    .viewer {
        width: 320px;
        margin: 10px;
        border: 3px solid #3a3a3a;
        border-radius: 5px;
        display: block;
    }
    img {
        max-width:100%;
        max-height:100%;
        vertical-align: bottom;
    }
    .button_holder {
        height: 90px;
        width: 90px;
        margin: 10px;
        border: 1px double black;
        display: inline-block;
    }
    button {
        all: unset;
        width: 60px;
        height: 24px;
        margin: 10px;
        padding: 6px;
        font-size: 1rem;
        text-align: center;
        color: ghostwhite;
        background: #363636;
        text-transform: uppercase;
        border-radius: 1em;
        font-family: 'Noto Sans KR', sans-serif;
        box-shadow: inset #6b6b6b 1px 1px 4px 4px;
    }
    button:hover {
        background: blue!important;
    }
    button:focus {
        background: navy!important;
    }
    button:active {
        background: darkgreen!important;
    }

    .grid {
        display: grid;
        grid-template-columns: 90px 90px 90px;
        align-content: center;
        justify-content: center;
        width: 320px;
        margin: 10px;
    }
    .remote {
        background: darkgray;
        width: 360px;
        padding: 10px;
        border-radius: 2em;
        border: 3px solid #4d4d4d;
    }
</style>
<div class="remote">
<div class="viewer">
    <img src="http://localhost:5000/video_feed" alt="TV Screen">
</div>
<div class="grid">
    <button id="input" on:click={pressButton}>Input</button>
    <div></div>
    <button id="power" on:click={pressButton} style="background: darkred; box-shadow: inset indianred 1px 1px 4px 4px;">Power</button>


    <div></div>
    <button id="up" on:click={pressButton}>Up</button>
    <div></div>

    <button id="left" on:click={pressButton}>Left</button>
    <button id="okay" on:click={pressButton}>Okay</button>
    <button id="right" on:click={pressButton}>Right</button>

    <div></div>
    <button id="down" on:click={pressButton}>Down</button>
    <div></div>

    <button id="back" on:click={pressButton}>Back</button>
    <div></div>
    <button id="info" on:click={pressButton}>Info</button>

    <button id="vol_up" on:click={pressButton}>Vol +</button>
    <div></div>
    <button id="ch_up" on:click={pressButton}>CH +</button>

    <button id="vol_down" on:click={pressButton}>Vol -</button>
    <div></div>
    <button id="ch_down" on:click={pressButton}>CH -</button>

</div>
</div>