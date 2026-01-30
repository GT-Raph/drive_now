import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:drive_now/core/network/api_service.dart';

class UploadDocumentsScreen extends StatefulWidget {
  const UploadDocumentsScreen({super.key});

  @override
  State<UploadDocumentsScreen> createState() => _UploadDocumentsScreenState();
}

class _UploadDocumentsScreenState extends State<UploadDocumentsScreen> {
  final picker = ImagePicker();
  File? ghanaCard, license, selfie, bill;

  Future<void> pick(String type) async {
    final picked = await picker.pickImage(source: ImageSource.camera);
    if (picked == null) return;

    final file = File(picked.path);
    final success = await ApiService.uploadDocument(file, type);

    if (success) {
      setState(() {
        if (type == 'ghana_card') ghanaCard = file;
        if (type == 'license') license = file;
        if (type == 'selfie') selfie = file;
        if (type == 'bill') bill = file;
      });
    }
  }

  Widget card(String title, String type, File? file) {
    return GestureDetector(
      onTap: () => pick(type),
      child: Container(
        height: 120,
        margin: const EdgeInsets.only(bottom: 16),
        decoration: BoxDecoration(
          border: Border.all(color: Colors.red),
          borderRadius: BorderRadius.circular(12),
        ),
        child: Center(
          child: file == null
              ? Text('Upload $title')
              : Image.file(file, fit: BoxFit.cover),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Driver Verification')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            card('Ghana Card', 'ghana_card', ghanaCard),
            card('Driver License', 'license', license),
            card('Selfie', 'selfie', selfie),
            card('Utility Bill', 'bill', bill),
            ElevatedButton(
              onPressed: () => Navigator.pop(context),
              child: const Text('Next'),
            ),
          ],
        ),
      ),
    );
  }
}
