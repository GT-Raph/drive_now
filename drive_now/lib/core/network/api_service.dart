import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:drive_now/core/storage/auth_storage.dart';

class ApiService {
  static const String baseUrl = 'http://10.0.2.2:8000/api/v1';

  /// Verify OTP
  static Future<Map<String, dynamic>?> verifyOtp({required String otp}) async {
    final response = await http.post(
      Uri.parse('$baseUrl/auth/verify-otp'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'otp': otp}),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    }
    return null;
  }

  /// Request OTP (Email or SMS)
  static Future<bool> requestOtp({
    required String fullName,
    required String email,
    required String phone,
    required String method, // "email" or "sms"
  }) async {
    final response = await http.post(
      Uri.parse('$baseUrl/auth/request-otp'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'full_name': fullName,
        'email': email,
        'phone': phone,
        'method': method,
      }),
    );

    return response.statusCode == 200;
  }

  //SEND JWT WITH PROTECTED REQUESTS
  static Future<http.Response> authorizedPost(
    String endpoint,
    Map<String, dynamic> body,
  ) async {
    final token = await AuthStorage.getToken();

    return http.post(
      Uri.parse('$baseUrl$endpoint'),
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer $token',
      },
      body: jsonEncode(body),
    );
  }

  /// Complete Driver Profile
  static Future<bool> completeDriverProfile({
    required String licenseNumber,
    required String vehicleType,
    required String vehiclePlate,
  }) async {
    final response = await authorizedPost('/drivers/complete-profile', {
      'license_number': licenseNumber,
      'vehicle_type': vehicleType,
      'vehicle_plate': vehiclePlate,
    });

    return response.statusCode == 200;
  }

  /// Get Dashboard Data
  static Future<Map<String, dynamic>> getDashboard() async {
    final token = await AuthStorage.getToken();
    final res = await http.get(
      Uri.parse('$baseUrl/drivers/dashboard'),
      headers: {'Authorization': 'Bearer $token'},
    );
    return jsonDecode(res.body);
  }

  /// Upload Document
  static Future<bool> uploadDocument(File file, String type) async {
    final token = await AuthStorage.getToken();
    final request = http.MultipartRequest(
      'POST',
      Uri.parse('$baseUrl/drivers/upload-document'),
    );

    request.headers['Authorization'] = 'Bearer $token';
    request.fields['type'] = type;
    request.files.add(await http.MultipartFile.fromPath('file', file.path));

    final res = await request.send();
    return res.statusCode == 200;
  }
}
