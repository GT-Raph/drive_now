// import 'package:drive_now/core/widgets/splash_decider.dart';

import '../features/splash/splash_decider.dart';
import '../features/onboarding/welcome_screen.dart';
// import '../features/auth/login_screen.dart';
import '../features/auth/register_screen.dart';
import '../features/profile/complete_profile_screen.dart';
import 'package:drive_now/features/auth/otp_verification_screen.dart';

final appRoutes = {
  '/': (context) => const SplashDecider(),
  '/welcome': (context) => const WelcomeScreen(),
  // '/login': (context) => const LoginScreen(),
  '/register': (context) => const RegisterScreen(),
  '/otp': (context) => const OtpVerificationScreen(),
  '/complete-profile': (context) => const CompleteProfileScreen(),
  // '/home': (_) => const HomeScreen(),
};
