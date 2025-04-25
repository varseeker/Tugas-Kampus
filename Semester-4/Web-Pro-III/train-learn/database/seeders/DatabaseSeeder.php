<?php

namespace Database\Seeders;

use App\Models\Kategori;
use App\Models\User;
// use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     */
    public function run(): void
    {
        // User::factory(10)->create();

        // USER
        User::factory()->create([
            'nama' => 'Administrator',
            'email' => 'admin@gmail.com',
            'role' => '1',
            'status' => 1,
            'hp' => '085123123123',
            'password' => bcrypt('admin'),
        ]);
        User::factory()->create([
            'nama' => 'Azure',
            'email' => 'azurelights21@gmail.com',
            'role' => '0',
            'status' => 1,
            'hp' => '085773590904',
            'password' => bcrypt('azurelights'),
        ]);

        // KATEGORI
        Kategori::create([
            'nama_kategori' => 'Monitor'
        ]);
        Kategori::create([
            'nama_kategori' => 'Keyboard'
        ]);
        Kategori::create([
            'nama_kategori' => 'Flashdisk'
        ]);
        Kategori::create([
            'nama_kategori' => 'Mouse'
        ]);
        Kategori::create([
            'nama_kategori' => 'Cooling Pad'
        ]);
    }
}
