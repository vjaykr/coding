package com.example.neat1stcalculator;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText text1, text2;
    TextView text3;
    Button addb, substractb, multiplyb, divideb;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);

        // Initializing views
        text1 = findViewById(R.id.text1);
        text2 = findViewById(R.id.text2);
        text3 = findViewById(R.id.text3);

        addb = findViewById(R.id.addb);
        substractb = findViewById(R.id.substractb);
        multiplyb = findViewById(R.id.multiplyb);
        divideb = findViewById(R.id.divideb);

        // Add button click listener
        addb.setOnClickListener(view -> {
            try {
                int a = Integer.parseInt(text1.getText().toString());
                int b = Integer.parseInt(text2.getText().toString());
                int c = a + b;
                text3.setText(String.valueOf(c));
            } catch (NumberFormatException e) {
                showErrorMessage();
            }
        });

        // Subtract button click listener
        substractb.setOnClickListener(view -> {
            try {
                int a = Integer.parseInt(text1.getText().toString());
                int b = Integer.parseInt(text2.getText().toString());
                int c = a - b;
                text3.setText(String.valueOf(c));
            } catch (NumberFormatException e) {
                showErrorMessage();
            }
        });

        // Multiply button click listener
        multiplyb.setOnClickListener(view -> {
            try {
                int a = Integer.parseInt(text1.getText().toString());
                int b = Integer.parseInt(text2.getText().toString());
                int c = a * b;
                text3.setText(String.valueOf(c));
            } catch (NumberFormatException e) {
                showErrorMessage();
            }
        });

        // Divide button click listener
        divideb.setOnClickListener(view -> {
            try {
                int a = Integer.parseInt(text1.getText().toString());
                int b = Integer.parseInt(text2.getText().toString());
                if (b != 0) {
                    float c = (float) a / b;
                    text3.setText(String.valueOf(c));
                } else {
                    text3.setText("Cannot divide by zero");
                }
            } catch (NumberFormatException e) {
                showErrorMessage();
            }
        });
    }

    // Helper method to show error message
    private void showErrorMessage() {
        Toast.makeText(this, "Please enter valid numbers", Toast.LENGTH_SHORT).show();
    }
}
