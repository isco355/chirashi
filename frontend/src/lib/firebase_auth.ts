import { getAuth, GoogleAuthProvider, signInWithPopup } from 'firebase/auth';
import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
import { goto } from '$app/navigation';

const firebaseConfig = {
  apiKey: "AIzaSyBcXfYDdF7s6Z72_GND5Qd7oUK4fGAbVfU",
  authDomain: "eazy-6a1be.firebaseapp.com",
  projectId: "eazy-6a1be",
  storageBucket: "eazy-6a1be.firebasestorage.app",
  messagingSenderId: "669901000452",
  appId: "1:669901000452:web:05cd10b21b6f5d83928a51",
  measurementId: "G-BH73PLTG0J"
};
// Initialize Firebase
export const app = initializeApp(firebaseConfig);
// const firestore = getFirestore(app);
export const auth = getAuth(app);
export async function signInWithGoogle(auth: any) {
  const googleProvider = new GoogleAuthProvider();
  try {
    const user = await signInWithPopup(auth, googleProvider);
    console.log(user)
    goto('/Explore')
  } catch (e) {

    console.log(e)
  }
}

export const handleSignOut = (signout: any) => {
  signout()
  goto('/')
}
