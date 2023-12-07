from onvif import ONVIFCamera
import sys
import time

def move_camera(pan, tilt, zoom):
    try:
        mycam = ONVIFCamera('192.168.12.7', 80, 'admin', 'admin')

        # Get the media and PTZ services
        media = mycam.create_media_service()
        ptz = mycam.create_ptz_service()

        # Get the default media profile
        media_profile = media.GetProfiles()[0]
        reference_token=media_profile.token

        # Get the current PTZ position
        current_position = ptz.GetStatus({'ProfileToken': media_profile.token}).Position
        #print('Current PTZ position:', current_position)

        # Create an AbsoluteMove request
        moverequest = ptz.create_type('AbsoluteMove')
        moverequest.ProfileToken = media_profile.token
        moverequest.Position = current_position

        # Set the target PTZ position
        moverequest.Position.PanTilt.x = float(pan)
        moverequest.Position.PanTilt.y = float(tilt)
        moverequest.Position.Zoom.x = float(zoom)
        response = ptz.AbsoluteMove(moverequest)
        #print('AbsoluteMove response:', response)


    except Exception as e:
        print('Error:', e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 camera.py <pan> <tilt> <zoom>")
    else:
        pan, tilt, zoom = sys.argv[1], sys.argv[2], sys.argv[3]
        move_camera(pan, tilt, zoom)

