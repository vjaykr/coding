package com.example.myrecycler;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class MyAdapter extends RecyclerView.Adapter<MyViewHolder> {

    Context context;
    List <Items> ItemsList;

    public MyAdapter(Context context, List<Items> itemsList) {
        this.context = context;
        ItemsList = itemsList;
    }

    @NonNull
    @Override
    public MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {

        return new MyViewHolder(LayoutInflater.from(context).inflate(R.layout.items,parent,false));
    }

    @Override
    public void onBindViewHolder(@NonNull MyViewHolder holder, int position)
    {
        holder.imageView.setImageResource(ItemsList.get(position).getImageView());
        holder.nameView.setText(ItemsList.get(position).getNameView());
        holder.descView.setText(ItemsList.get(position).getDescView());

    }

    @Override
    public int getItemCount() {
        return ItemsList.size();
    }
}
