<?php

namespace App\Contracts\Auth;
use Illuminate\Contracts\Auth\Authenticatable;
use Illuminate\Contracts\Auth\UserProvider;

interface IotUserApiCountract extends  UserProvider
{
    public function retrieveById($identifier);

    public function retrieveByCredentials(array $credentials);
  
    public function validateCredentials(Authenticatable $user, array $credentials);
  
    public function retrieveByToken($identifier, $token);
  
    public function updateRememberToken(Authenticatable $user, $token);
}
