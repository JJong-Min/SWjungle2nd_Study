import "./card.css";
import Heart from "../../img/heart.svg";
import HeartFilled from "../../img/heartFilled.svg";
import Comment from "../../img/comment.svg";
import Share from "../../img/share.svg";
import Info from "../../img/info.svg";

const Card = ({post}) => {
    return (
        <div className="card">
            <div className="info">
                <img src={post.userImg} alt="" classname="userImg"></img>
                <span>{post.fullname}</span>
            </div>
            <img src={post.postImg} alt="" classname="postImg"></img>
        <div className="interation">
        <img src={Heart} alt="" classname="cardIcon"></img>
        <img src={Comment} alt="" classname="cardIcon"></img>
        <img src={Share} alt="" classname="cardIcon"></img>
        <img src={Info} alt="" classname="cardIcon"></img>
        </div>
        </div>
    )
}

export default Card