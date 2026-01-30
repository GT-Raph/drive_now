import 'package:flutter/material.dart';
import 'package:drive_now/core/network/api_service.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  bool loading = true;
  Map<String, dynamic>? dashboard;

  @override
  void initState() {
    super.initState();
    loadDashboard();
  }

  Future<void> loadDashboard() async {
    dashboard = await ApiService.getDashboard();
    setState(() => loading = false);
  }

  @override
  Widget build(BuildContext context) {
    if (loading) {
      return const Scaffold(body: Center(child: CircularProgressIndicator()));
    }

    final approved = dashboard!['approved'];
    final vehicleAssigned = dashboard!['vehicle_assigned'];

    return Scaffold(
      appBar: AppBar(title: const Text('Dashboard')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            if (!approved)
              _infoCard(
                'Verification in Progress',
                'Your documents are under review',
                Colors.orange,
              ),
            if (approved && !vehicleAssigned)
              _infoCard(
                'No Vehicle Assigned',
                'A vehicle will be assigned to you soon',
                Colors.blue,
              ),
          ],
        ),
      ),
    );
  }

  Widget _infoCard(String title, String message, Color color) {
    return Card(
      color: color.withOpacity(0.1),
      child: ListTile(
        title: Text(title, style: const TextStyle(fontWeight: FontWeight.bold)),
        subtitle: Text(message),
      ),
    );
  }
}
