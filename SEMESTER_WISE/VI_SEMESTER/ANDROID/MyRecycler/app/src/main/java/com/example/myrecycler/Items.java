package com.example.myrecycler;

public class Items {

    String nameView;

    String descView;
    int imageView;

    public Items(String nameView, String descView, int imageView) {
        this.nameView = nameView;
        this.descView = descView;
        this.imageView = imageView;
    }

    public String getNameView() {
        return nameView;
    }

    public void setNameView(String nameView) {
        this.nameView = nameView;
    }

    public String getDescView() {
        return descView;
    }

    public void setDescView(String descView) {
        this.descView = descView;
    }

    public int getImageView() {
        return imageView;
    }

    public void setImageView(int imageView) {
        this.imageView = imageView;
    }


}
