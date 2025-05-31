<script>
  import { onMount } from "svelte";
  const localhost= import.meta.env.VITE_LOCALHOST
  const request_path =localhost+"/fliers"

  
  
  let fliers = $state([]);
  onMount(async function () {
    console.log(
'fetching flyers'
    )
  let rquestFlier= await fetch(request_path).then(data=> data.json())
    .then(data=>{
      fliers=data
  })
  })
  </script>









  <main>
    <h1>Filter </h1>
    <button >Filter </button>
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
