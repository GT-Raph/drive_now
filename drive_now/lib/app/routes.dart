import '../features/onboarding/splash_screen.dart';
import '../features/onboarding/welcome_screen.dart';
// import '../features/auth/login_screen.dart';
import '../features/auth/register_screen.dart';
import 'package:drive_now/features/auth/otp_verification_screen.dart';

final appRoutes = {
  '/': (context) => const SplashScreen(),
  '/welcome': (context) => const WelcomeScreen(),
  // '/login': (context) => const LoginScreen(),
  '/register': (context) => const RegisterScreen(),
  '/otp': (context) => const OtpVerificationScreen(),
};
