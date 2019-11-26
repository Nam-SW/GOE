package com.example.goe;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.Toast;

import com.google.android.material.floatingactionbutton.FloatingActionButton;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageButton btnElectryuse = findViewById(R.id.imageButton4);
        ImageButton btnSolution = findViewById(R.id.imageButton3);
        ImageButton btnBilluse = findViewById(R.id.imageButton2);

        FloatingActionButton btnSetting = findViewById(R.id.floatingActionButton2);

        btnSetting.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(), "미개발",Toast.LENGTH_LONG).show();
            }
        });

        btnElectryuse.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this,ElectryUse_Activity.class );
                startActivity(intent);
            }
        });

        btnSolution.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this,Solution_Activity.class );
                startActivity(intent);
            }
        });

        btnBilluse.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this,Billuse_Activity.class );
                startActivity(intent);
            }
        });
    }
}
