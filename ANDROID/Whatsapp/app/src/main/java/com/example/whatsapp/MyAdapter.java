package com.example.whatsapp;


import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.lifecycle.Lifecycle;
import androidx.viewpager2.adapter.FragmentStateAdapter;

public class MyAdapter extends FragmentStateAdapter {

    private static final int nTabs = 3;


    public MyAdapter(@NonNull FragmentManager fragmentManager, @NonNull Lifecycle lifecycle) {
        super(fragmentManager, lifecycle);
    }

    @NonNull
    @Override
    public Fragment createFragment(int position) {
        switch (position){
            case 1: return new Chats();
            case 2: return new Status();
            case 3: return new Calls();
            default: return new Chats();
        }
    }

    @Override
    public int getItemCount() {
        return nTabs;
    }
}
