<script>
import { onMount } from "svelte";
const localhost= "http://localhost:8000"
const request_path =localhost+"/fliers"

let fliers =$state([]);
onMount(async function () {
let rquestFlier= await fetch(request_path).then(data=> data.json())
  .then(data=>{
    fliers=data
})
})
</script>









<div class="h-screen w-full  flex flex-col  items-center justify-around gap-30">
<h1 class="font-bold 
text-5xl
">OpenShelf</h1>

<div
class="w-9/10 grid grid-flow-row grid-cols-4 gap-4 "
>
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
</div>
