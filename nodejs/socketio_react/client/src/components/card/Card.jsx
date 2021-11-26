import "./card.css";
import Heart from "../../img/heart.svg";
import HeartFilled from "../../img/heartFilled.svg";
import Comment from "../../img/comment.svg";
import Share from "../../img/share.svg";
import Info from "../../img/info.svg";
import { useState } from "react";

const Card = ({post}) => {
    const [liked, sektLiked] = useState(false);
    return (
        <div className="card">
            <div className="info">
                {/* <img src={post.userImg} alt="" classname="userImg" /> */}
                <span>{post.fullname}</span>
            </div>
            {/* <img src={post.postImg} alt="" classname="postImg" /> */}
        <div className="interaction">
            {liked ? (<img src={HeartFilled} alt="" classname="cardIcon" />
            ) : (
                <img src={Heart} alt="" classname="cardIcon" />
            )}
            
            <img src={Comment} alt="" classname="cardIcon" />
            <img src={Share} alt="" classname="cardIcon" />
            <img src={Info} alt="" classname="cardIcon infoIcon" />
        </div>
        </div>
    )
}

export default Card