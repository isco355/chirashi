
<script lang="ts">
	import '../app.css';
	
	let { children } = $props();
</script>



<nav>
	<h1> OpenShelf </h1>
	
	<ul>
		<li>
			<a href="/Home" > Home</a>
		</li>
		<li>
			<a href="/Explore" > Explore</a>
		</li>
		<li>
			<a href="/UploadScan" > Upload Scan</a>
		</li>
		<li>
			<a href="/UserProfile" > Profile</a>
		</li>
	</ul>
  
</nav>	

{@render children()}


  
<style>
  nav
  {
	display: flex;
	 background-color: green;
	 color: white;
	 font-size: 1.5rem;
  }
 
  ul{
	display: flex;
	list-style: none;
	margin: 0;
	margin-left: auto;
	
	
   }
   li
   {
	margin-right:30px;
	
   }
   h1
   {
	margin-right:30px;
	margin: 0;
	font-size: 1em;
	font-weight: normal;
   }
 
  </style>  

