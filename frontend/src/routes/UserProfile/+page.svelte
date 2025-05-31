<script>
    import { SignedIn,SignedOut } from 'sveltefire';

    import {signInWithGoogle} from '$lib/firebase_auth.ts'
</script>

<SignedIn let:user>
  <div class="h-screen flex flex-col justify-around place-items-center">

		<img class="h-25 w-25 rounded-full" src={user.photoURL}/>	
    <p>Howdy, {user.displayName}</p>
    <p> {user.email}</p>
</div>
</SignedIn>

