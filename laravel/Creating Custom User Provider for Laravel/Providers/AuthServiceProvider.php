<?php

namespace App\Providers;

// use Illuminate\Support\Facades\Gate;

use App\Services\Auth\IotUserApiService;
use Illuminate\Foundation\Support\Providers\AuthServiceProvider as ServiceProvider;
use Illuminate\Support\Facades\Auth;

class AuthServiceProvider extends ServiceProvider
{
    /**
     * The model to policy mappings for the application.
     *
     * @var array<class-string, class-string>
     */
    protected $policies = [
        // 'App\Models\Model' => 'App\Policies\ModelPolicy',
    ];

    /**
     * Register any authentication / authorization services.
     *
     * @return void
     */
    
    public function boot()
    {
        $this->registerPolicies();

        Auth::provider('iotUserApi', function($app, array $config) {
            return new IotUserApiService();
        });
    }
}
