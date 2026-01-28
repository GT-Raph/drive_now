import 'package:flutter_test/flutter_test.dart';
import 'package:drive_now/app/app.dart';

void main() {
  testWidgets('DriveNow app builds', (WidgetTester tester) async {
    await tester.pumpWidget(const DriveNowApp());
    expect(find.byType(Object), findsWidgets);
  });
}
