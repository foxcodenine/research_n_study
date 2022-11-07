<?php

namespace App\Services\Auth;

use App\Contracts\Auth\IotUserApiCountract;
use App\Models\User;
use Illuminate\Contracts\Auth\Authenticatable;
use Illuminate\Support\Facades\Http;



/**
 * Class IotUserApiService.
 */
class IotUserApiService implements IotUserApiCountract
{
    /**
     * retrieveById will be called on every request where the session 
     * cookie has information about user id
     */
    public function retrieveById($identifier){
        
        $currentUser = unserialize(session('currentUser'));

        if ($identifier == $currentUser->id) {
            return $currentUser;
        } 

        session()->invalidate();
        session()->regenerateToken();
        return false;                
    }
    // _________________________________________________________________

    /**
     * retrieveByCredentials will be called on login, it calls the custom 
     * method 'retrieveIotUserFromApi' that return a the User if authenticated
     */
    public function retrieveByCredentials(array $credentials) {       
        
        return $this->retrieveIotUserFromApi(
            $credentials['email'],  $credentials['password']
        );
    }

    // _________________________________________________________________


    /**
     * If Authentcated user provided it is save in session as currentUser
     */
    public function validateCredentials(Authenticatable $user, array $credentials) {
        
        if(is_null($user)) { return false; }

        session(['currentUser' => serialize($user)]);
        return true;
    }

    // _________________________________________________________________

  
    public function retrieveByToken($identifier, $token){
        // Not implemented
    }
    
  
    public function updateRememberToken(Authenticatable $user, $token){
        // Not implemented
    }

    // _________________________________________________________________

    /**
     * My custom function, fetch user credentials from api, 
     * and create a user instance with fetched data
     */
    public function retrieveIotUserFromApi($email, $password) {
        
        $url = env('IOT_APP_BASE_URL') . '/api' . '/sso/login';

        $response = Http::post($url,[
			'email' => $email,
			'password' => $password
		]);


        if ($response->status() === 200) {
            $responseUser = json_decode($response->body());
            return new User($responseUser);
        }

        return null;
    }

    // _________________________________________________________________
}