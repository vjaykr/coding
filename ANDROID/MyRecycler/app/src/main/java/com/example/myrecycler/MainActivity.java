package com.example.myrecycler;




import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {


    RecyclerView recyclerView;
    List<Items> itemsList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        recyclerView = findViewById(R.id.myrecycler);
        itemsList = new ArrayList<>();

        itemsList.add(new Items("German","Dog_prajati",R.drawable.img));
        itemsList.add(new Items("kalo","Dog_prajati",R.drawable.img_1));
        itemsList.add(new Items("munja","Dog_prajati",R.drawable.img_2));
        itemsList.add(new Items("john","Dog_prajati",R.drawable.img_4));
        itemsList.add(new Items("kitty","Dog_prajati",R.drawable.img_5));
        itemsList.add(new Items("lili","Dog_prajati",R.drawable.img_7));
        itemsList.add(new Items("bull_Dog","Dog_prajati",R.drawable.img_8));
        itemsList.add(new Items("Pit","Dog_prajati",R.drawable.img_9));
        itemsList.add(new Items("RedRetriver","Dog_prajati",R.drawable.img_10));
        itemsList.add(new Items("juli","Dog_prajati",R.drawable.img_11));
        itemsList.add(new Items("tony","Dog_prajati",R.drawable.img_12));



        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        recyclerView.setAdapter(new MyAdapter(MainActivity.this,itemsList));



    }
}