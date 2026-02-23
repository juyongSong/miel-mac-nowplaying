import subprocess

def get_now_playing():
    """현재 macOS에서 재생 중인 미디어 제목과 상태를 가져옵니다."""
    swift_code = r"""
    import Foundation
    let path = "/System/Library/PrivateFrameworks/MediaRemote.framework"
    let url = NSURL(fileURLWithPath: path)
    if let bundle = CFBundleCreate(kCFAllocatorDefault, url) {
        let funcName = "MRMediaRemoteGetNowPlayingInfo" as CFString
        if let funcPtr = CFBundleGetFunctionPointerForName(bundle, funcName) {
            typealias MRGetNowPlayingInfoFunction = @convention(c) (DispatchQueue, @escaping ([String: Any]) -> Void) -> Void
            let getNowPlayingInfo = unsafeBitCast(funcPtr, to: MRGetNowPlayingInfoFunction.self)
            let sema = DispatchSemaphore(value: 0)
            
            getNowPlayingInfo(DispatchQueue.global()) { info in
                let title = info["kMRMediaRemoteNowPlayingInfoTitle"] as? String ?? ""
                let artist = info["kMRMediaRemoteNowPlayingInfoArtist"] as? String ?? ""
                
                // 재생 속도(Playback Rate) 확인: 0.0 이면 일시정지
                let rate = info["kMRMediaRemoteNowPlayingInfoPlaybackRate"] as? Double ?? 0.0
                
                if rate == 0.0 && !title.isEmpty {
                    print("PAUSED") 
                } else if !title.isEmpty {
                    print(artist.isEmpty ? title : "\(artist) - \(title)")
                }
                sema.signal()
            }
            _ = sema.wait(timeout: .now() + 2)
        }
    }
    """
    try:
        result = subprocess.run(
            ["swift", "-"],
            input=swift_code,
            text=True,
            capture_output=True,
            check=True
        )
        return result.stdout.strip()
    except Exception as e:
        return None