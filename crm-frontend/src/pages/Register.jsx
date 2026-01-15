import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";

const Register = () => {
    const navigate = useNavigate();

    const [formData, setFormData] = useState({
        username: "",
        email: "",
        password: "",
        role: "sales",
    });

    const [error, setError] = useState("");

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError("");

        try {
            await api.post("auth/register/", formData);
            alert("User registered successfully");
            navigate("/login");
        } catch (err) {
            const data = err.response?.data;

            if (data) {
                const field = Object.keys(data)[0];       // e.g. "password"
                const message = data[field][0];           // error text

                // Capitalize field name
                const fieldName =
                    field.charAt(0).toUpperCase() + field.slice(1);

                setError(`${fieldName}: ${message}`);
            } else {
                setError("Registration failed. Try again.");
            }
        }

    };


    return (
        <div className="auth-container">
            <form className="auth-card" onSubmit={handleSubmit}>
                <h2>Register User</h2>

                <div className="form-group">
                    <label>Username</label>
                    <input
                        type="text"
                        name="username"
                        value={formData.username}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label>Email</label>
                    <input
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                    />
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input
                        type="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label>Role</label>
                    <select name="role" value={formData.role} onChange={handleChange}>
                        <option value="sales">Sales</option>
                        <option value="manager">Manager</option>
                        <option value="admin">Admin</option>
                    </select>
                </div>

                {error && <p className="error">{error}</p>}

                <button type="submit" className="btn-primary">
                    Register
                </button>
            </form>
        </div>
    );
}

export default Register;
