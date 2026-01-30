import 'package:flutter/material.dart';
import 'routes.dart';
import 'theme.dart';

class DriveNowApp extends StatelessWidget {
  const DriveNowApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'DriveNow',
      debugShowCheckedModeBanner: false,
      theme: appTheme,
      routes: appRoutes,
      initialRoute: '/',
    );
  }
}
