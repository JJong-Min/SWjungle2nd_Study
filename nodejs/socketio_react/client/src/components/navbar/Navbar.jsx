import "./navbar.css"
import Notification from "../../img/notification.svg"

const Navbar = () => {
    return (
        <div className="navbar">
            <span className="logo">Lama App</span>
            <div className="icons">
                <div className="icon">
                    <img src={Notification} className="iconImg" alt="" />
                    <div className="counter">2</div>
                </div>
             </div>
        </div>
    )
} 

export default Navbar