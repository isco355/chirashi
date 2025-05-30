<script>
  
  import { onMount } from "svelte";


  const localhost= "http://localhost:8000/"
  const request_path =localhost+"/fliers"

  
  let count = $state(0);

  function increment() {
    count += 1;
  }
  
  let fliers = $state([]);
  onMount(async function () {
  let rquestFlier= await fetch(request_path).then(data=> data.json())
    .then(data=>{
      fliers=data
  })
  })
  </script>







<!--
  <div class="h-screen w-full  flex flex-col  items-center justify-around gap-30">
  <h1 class="font-bold text-5xl "> OpenShelf</h1>
!-->



  <main> <!--Button-HTML --> 
    <h1>Filter Demo {count} </h1>
    <button on:click={increment}>Filter </button>
  </main>
  




  <div class="w-9/10 grid grid-flow-row grid-cols-4 gap-4 ">



    
  {#each fliers as flier}
  
   <div class="max-w-sm bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow duration-300 border-solid border-1">
      <img
   src={flier.image_url}
        class="w-full  h-120 object-contain "
      />
      <div class="p-4">
        <p class="text-lg font-semibold text-gray-800">
      {flier.title}
                id: {flier.id}
        </p>
      </div>
    </div>
  {:else}
      <p>loading..</p>
  {/each}
  </div>
  <!-- </div>-->



  <style>  /* CSS  */
    main {

      padding: 2rem;
      font-family: sans-serif;
      
    }
  
    button {
      padding: 4px 8px;
      font-size: 1.2rem;
      
      cursor: pointer;
      background-color: #4caf50;
      color: white;
      border: 1px solid blue;
      border-radius: 5px;
    }
  
    button:hover {
      background-color: #45a049;
      
    }




 
</style>  