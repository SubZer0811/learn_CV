import cv2
import numpy as np
from matplotlib import pyplot as plt

def orb(fa, fb):
    
    orb = cv2.ORB_create()
    
    # f1 = cv2.imread("/home/sub0811/Desktop/opencv/motion/gate_1.jpeg")
    # f2 = cv2.imread("/home/sub0811/Desktop/opencv/motion/gate_2.jpeg")

    # print(fa.shape)
    # print(fb.shape)
    f1 = fa
    f2 = fb
    ft = fb
    
    w = f1.shape[0]
    h = f1.shape[1]

    kp1, des1 = orb.detectAndCompute(f1, None)
    kp2, des2 = orb.detectAndCompute(f2, None)

    bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, True)

    matches = bf.match(des1, des2)

    matches = sorted(matches, key = lambda x: x.distance)
    good_matches = matches[:5]

    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good_matches ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good_matches ]).reshape(-1,1,2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    
    matchesMask = mask.ravel().tolist()
    h,w = f1.shape[:2]
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)

    dst = cv2.perspectiveTransform(pts,M)
    
    draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                singlePointColor = None,
                matchesMask = matchesMask, # draw only inliers
                flags = 2)

    img3 = cv2.drawMatches(f1,kp1,f2,kp2,good_matches, None,**draw_params)

    cv2.imshow("img3", img3)

    b = list(dst[0])
    a = list(dst)
    # print(b)

    
    
    green = (0, 255, 0)
    rect = cv2.boundingRect(dst)
    # print(type(ft))
    # print(ft.shape)
    i = 0
    
    q, w, e, r = rect
    q = coords(q)
    w = coords(w)
    e = coords(e)
    r = coords(r)

    cv2.rectangle(ft, (q, w), (e, r), green, 3)
    cv2.imshow("current_frame", ft)
    # cv2.waitKey()
    
    return q, w, e, r

#####################################################################################################


def coords(i):

    if(i>0):
        return int(i)
    else:
        return 0



if __name__=="__main__":

    cap = cv2.VideoCapture('/home/sub0811/Desktop/opencv/Gate_Video/1.mp4')

    # frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    # frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))

    ret, frame = cap.read()
    ret, var_frame = cap.read()

    q, w, e, r = orb(frame, var_frame)

    roi_frame = var_frame[w:r, q:e]
    
    count = 1

    # print(x, y, w, h)
    # print(roi_frame.shape)
    # print(frame.shape)
    frame_count = 1
    
    while cap.isOpened():
        
        cv2.waitKey()
        q, w, e, r = orb(frame, roi_frame)
        # print(q, w, e, r)
        print(roi_frame.shape)
        # if(frame_count % 20 == 0):
        #     frame = var_frame
        ret, var_frame = cap.read()
        
        roi_frame = var_frame[w:r, q:e]
        
        cv2.imshow("roi_next_frame", roi_frame)

        frame_count = frame_count + 1
        print(frame_count)

        # if(frame_count > 180):
        #     cv2.waitKey()

        if cv2.waitKey(40) == 27:
            break

    cv2.destroyAllWindows()
    cap.release()