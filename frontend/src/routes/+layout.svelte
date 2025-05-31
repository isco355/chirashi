
<script lang="ts">
	import '../app.css';
	import { FirebaseApp } from 'sveltefire';
  import { SignedIn,SignedOut } from 'sveltefire';
  import {signInWithGoogle,handleSignOut,auth} from '$lib/firebase_auth.ts'
  import { onMount } from "svelte";

  import { page } from '$app/stores';
	let { children } = $props();
	

	console.log(auth)
</script>

<FirebaseApp {auth}>

<nav>
	
	<a href="/" > OpenShelf</a>
	<ul>
<SignedIn let:user  let:signOut>
		<li>
		</li>
		<li>
			<a href="/Explore" > Explore</a>
		</li>
		<li>
			<a href="/UploadScan" > Upload Scan</a>
		</li>
		<li>
					<div class="
 flex flex-row gap-2
">
			<a href="/UserProfile" > {user.displayName}</a>
		<img class="h-10 w-10 rounded-full" src={user.photoURL}/>	
</div>
		</li>

    <button on:click={()=>handleSignOut(signOut)}>Sign Out</button>
</SignedIn>
<SignedOut let:auth>
    <button  on:click={() => signInWithGoogle(auth)}>Sign In</button>
</SignedOut>


	</ul>
  
</nav>	

{#if $page.url.pathname === '/'}
{@render children()}
{:else}
<SignedIn >
{@render children()}
</SignedIn>
{/if}

</FirebaseApp>
  
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

