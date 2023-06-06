from procure import ZipSolution

class FlutterEngine(ZipSolution):
	path = 'depot/flutter-engine'
	url = 'https://storage.googleapis.com/flutter_infra_release/flutter/90fa3ae28fe6ddaee1af2c120f01e50201c1401b/windows-x64/windows-x64-embedder.zip'

solutions = [
    FlutterEngine,
]
