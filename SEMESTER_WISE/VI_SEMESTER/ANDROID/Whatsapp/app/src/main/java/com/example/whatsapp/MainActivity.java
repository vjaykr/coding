package com.example.whatsapp;

import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.viewpager2.widget.ViewPager2;

import com.google.android.material.tabs.TabLayout;
import com.google.android.material.tabs.TabLayoutMediator;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    TabLayout tabLayout;

    ViewPager2 viewPager2;

    ArrayList <String> arrayList;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        tabLayout = findViewById(R.id.mytab);
        viewPager2 = findViewById(R.id.myviewpg);
        arrayList = new ArrayList<>();

        arrayList.add("Chats");
        arrayList.add("Status");
        arrayList.add("Calls");

        MyAdapter adapter = new MyAdapter(getSupportFragmentManager(),getLifecycle());

        viewPager2.setAdapter(adapter);

        TabLayoutMediator tabLayoutMediator = new TabLayoutMediator(tabLayout,viewPager2,(tab,index)->{

            tab.setText((CharSequence) arrayList.get(index));
        });

        tabLayoutMediator.attach();

    }
}