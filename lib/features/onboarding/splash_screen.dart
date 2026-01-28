import 'package:flutter/material.dart';
import 'dart:async';

class SplashScreen extends StatefulWidget {
  const SplashScreen({super.key});

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();

    Timer(const Duration(seconds: 2), () {
      Navigator.pushReplacementNamed(context, '/welcome');
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Image.asset('assets/images/Drive_Now_Logo_white.png', width: 180),
            const SizedBox(height: 16),
            // const Text(
            //   'Empowering Drivers. Simplifying Ownership',
            //   style: TextStyle(fontSize: 12, color: Colors.black54),
            // ),
          ],
        ),
      ),
    );
  }
}
