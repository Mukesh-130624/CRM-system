import Navbar from "../components/Navbar";
import "./Dashboard.css";

export default function Dashboard() {
    return (
        <>
            <Navbar />
            <div className="dashboard-container">
                <h1>CRM Dashboard</h1>
                <p>Welcome to the CRM system.</p>
            </div>
        </>
    );
}
