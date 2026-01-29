import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = 'http://10.0.2.2:8000/api/v1';

  static Future<bool> registerDriver({
    required String fullName,
    required String email, // 👈 NEW
    required String phone,
    required String password,
  }) async {
    final response = await http.post(
      Uri.parse('$baseUrl/auth/register'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'full_name': fullName,
        'email': email, // 👈 NEW
        'phone': phone,
        'password': password,
      }),
    );

    return response.statusCode == 200;
  }
}
