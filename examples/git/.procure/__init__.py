from procure import ZipSolution

class FlutterEngine(ZipSolution):
	path = 'depot/flutter-engine'
	url = 'https://storage.googleapis.com/flutter_infra_release/flutter/080fbcb1759e5916f0d6cdcdfd945c053320e6b3/windows-x64/windows-x64-embedder.zip'

solutions = [
    FlutterEngine,
]
