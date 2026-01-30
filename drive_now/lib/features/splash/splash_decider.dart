import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class SplashDecider extends StatefulWidget {
  const SplashDecider({super.key});

  @override
  State<SplashDecider> createState() => _SplashDeciderState();
}

class _SplashDeciderState extends State<SplashDecider> {
  @override
  void initState() {
    super.initState();
    _decide();
  }

  Future<void> _decide() async {
    // Show splash for 2 seconds
    await Future.delayed(const Duration(seconds: 2));

    final prefs = await SharedPreferences.getInstance();

    final String? token = prefs.getString('access_token');
    final bool profileComplete = prefs.getBool('profile_complete') ?? false;

    if (!mounted) return;

    if (token == null) {
      // User not logged in
      Navigator.pushReplacementNamed(context, '/welcome');
    } else if (!profileComplete) {
      // Logged in but profile incomplete
      Navigator.pushReplacementNamed(context, '/complete-profile');
    } else {
      // Fully onboarded
      Navigator.pushReplacementNamed(context, '/home');
    }
  }

  @override
  Widget build(BuildContext context) {
    return const Scaffold(body: Center(child: CircularProgressIndicator()));
  }
}
