import { getAuth, GoogleAuthProvider, signInWithPopup, } from 'firebase/auth';
import { initializeApp, getApp, getApps } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
import { goto } from '$app/navigation';

const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN,
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID,
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID,
  appId: import.meta.env.VITE_FIREBASE_APP_ID,
  measurementId: import.meta.env.VITE_FIREBASE_APP_ID,
};

let app;
if (getApps().length === 0) {
  // If no apps are initialized, initialize a new app
  app = initializeApp(firebaseConfig);
} else {
  // If an app is already initialized, use the existing app
  app = getApp();
}

// export const app = initializeApp(firebaseConfig);
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
