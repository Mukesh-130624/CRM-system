import { Link } from "react-router-dom";
import { useContext } from "react";
import { AuthContext } from "../auth/AuthContext";
import "./Navbar.css";

const Navbar = () => {
    const { logout } = useContext(AuthContext);

    return (
        <nav className="navbar">
            <div className="navbar-container">
                <div className="nav-links">
                    <Link to="/dashboard">Dashboard</Link>
                    <Link to="/leads">Leads</Link>
                    <Link to="/customers">Customers</Link>
                    <Link to="/deals">Deals</Link>
                    <Link to="/tasks">Tasks</Link>
                </div>

                <button className="logout-btn" onClick={logout}>
                    Logout
                </button>
            </div>
        </nav>
    );
};

export default Navbar;
