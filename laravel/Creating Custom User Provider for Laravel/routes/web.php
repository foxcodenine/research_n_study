<?php

use App\Http\Controllers\DashboardController;
use App\Http\Controllers\ImagesController;
use App\Http\Controllers\TestController;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Auth;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

// ---------------------------------------------------------------------

Route::get('/', function () { return redirect(route('dashboard')); })->name('index');

Route::get('/home', function () { return redirect(route('dashboard')); })->name('home');



// ---------------------------------------------------------------------
// ----- Auth - routes

Auth::routes();

// ---------------------------------------------------------------------
// ----- Dashboard pages - routes

Route::get('/map', [DashboardController::class, 'map']  )->name('map');




