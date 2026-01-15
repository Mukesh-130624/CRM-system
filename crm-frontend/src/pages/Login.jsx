import { useState, useContext } from "react";
import { login } from "../api/auth";
import { AuthContext } from "../auth/AuthContext";
import { useNavigate } from "react-router-dom";

const Login = () => {
    const [form, setForm] = useState({
        username: "",
        password: "",
    });

    const [error, setError] = useState("");
    const { loginUser } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleChange = (e) => {
        setForm({
            ...form,
            [e.target.name]: e.target.value,
        });
    };

    const submit = async (e) => {
        e.preventDefault();
        setError("");

        try {
            const res = await login(form);
            loginUser(res.data);
            navigate("/dashboard");
        } catch (err) {
            console.error(err.response?.data);
            setError("Invalid username or password");
        }
    };

    return (
        <div className="auth-container">
            <form className="auth-card" onSubmit={submit}>
                <h2>Login</h2>

                <div className="form-group">
                    <label>Username</label>
                    <input
                        type="text"
                        name="username"
                        value={form.username}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input
                        type="password"
                        name="password"
                        value={form.password}
                        onChange={handleChange}
                        required
                    />
                </div>

                {error && <p className="error">{error}</p>}

                <button type="submit" className="btn-primary">
                    Login
                </button>
            </form>
        </div>
    );
};

export default Login;
