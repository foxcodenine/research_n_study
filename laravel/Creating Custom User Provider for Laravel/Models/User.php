<?php

namespace App\Models;

// use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Laravel\Sanctum\HasApiTokens;


class User extends Authenticatable
{
    use HasApiTokens, HasFactory, Notifiable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array<int, string>
     */
    protected $fillable = [
        'name',
        'email',
        'password',
    ];

    /**
     * The attributes that should be hidden for serialization.
     *
     * @var array<int, string>
     */
    protected $hidden = [
        'password',
        'remember_token',
    ];

    /**
     * The attributes that should be cast.
     *
     * @var array<string, string>
     */
    protected $casts = [
        'email_verified_at' => 'datetime',
    ];

    public function __construct(Object $objectData)
    {
        $this->id                       = $objectData->id;
        $this->email                    = $objectData->email;
        $this->organisation_id          = $objectData->organisation_id;
        $this->dashboard_access_level   = $objectData->dashboard_access_level;
        $this->mobile_app_access_level  = $objectData->mobile_app_access_level;
        $this->enabled                  = $objectData->enabled;
        $this->email_verified            = $objectData->email_verified;
        $this->organisation_name        = $objectData->organisation_name;
    }
}
