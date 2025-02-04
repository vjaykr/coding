package com.example.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

public class MainActivity extends AppCompatActivity {

    EditText edt1, edt2, edt3;
    Button btn;

    FirebaseAuth firebaseAuth;  // Declare FirebaseAuth instance

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize views
        edt1 = findViewById(R.id.myedt);   // Name
        edt2 = findViewById(R.id.myedt2); // Email
        edt3 = findViewById(R.id.myedt3); // Password
        btn = findViewById(R.id.mybtn);

        // Initialize FirebaseAuth
        firebaseAuth = FirebaseAuth.getInstance();

        // Button Click Listener
        btn.setOnClickListener(v -> {
            String name = edt1.getText().toString().trim();
            String email = edt2.getText().toString().trim();
            String pass = edt3.getText().toString().trim();

            // Input Validation
            if (name.isEmpty() || email.isEmpty() || pass.isEmpty()) {
                Toast.makeText(MainActivity.this, "All fields are required!", Toast.LENGTH_SHORT).show();
                return;
            }
            if (pass.length() < 6) {
                Toast.makeText(MainActivity.this, "Password must be at least 6 characters!", Toast.LENGTH_SHORT).show();
                return;
            }

            // Firebase Authentication - Create User
            firebaseAuth.createUserWithEmailAndPassword(email, pass)
                    .addOnCompleteListener(task -> {
                        if (task.isSuccessful()) {
                            FirebaseUser user = firebaseAuth.getCurrentUser();
                            Toast.makeText(MainActivity.this, "User Registered: " + user.getEmail(), Toast.LENGTH_SHORT).show();

                            // Pass Name to Next Activity
                            Intent intent = new Intent(MainActivity.this, MainActivity2.class);
                            intent.putExtra("key", name);
                            startActivity(intent);
                        } else {
                            Toast.makeText(MainActivity.this, "Error: " + task.getException().getMessage(), Toast.LENGTH_LONG).show();
                        }
                    });
        });
    }
}
