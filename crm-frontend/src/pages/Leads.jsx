import { useEffect, useState } from "react";
import {
    getLeads,
    createLead,
    updateLead,
    deleteLead,
    convertLead,
} from "../api/leads";
import Navbar from "../components/Navbar";

export default function Leads() {
    const [leads, setLeads] = useState([]);
    const [error, setError] = useState(null);

    const [form, setForm] = useState({
        name: "",
        email: "",
        phone: "",
    });

    /* ========================
       FETCH LEADS
    ======================== */
    const fetchLeads = async () => {
        try {
            const res = await getLeads();
            setLeads(res.data);
        } catch (err) {
            setError("Failed to load leads");
        }
    };

    useEffect(() => {
        fetchLeads();
    }, []);

    /* ========================
       FORM HANDLING
    ======================== */
    const handleChange = (e) => {
        setForm({
            ...form,
            [e.target.name]: e.target.value,
        });
    };

    /* ========================
       CREATE LEAD
    ======================== */
    const addLead = async () => {
        const result = await createLead(form);

        if (!result.success) {
            setError(result.error);
            return;
        }

        setError(null); // clear only on success
        fetchLeads();
        setForm({ name: "", email: "", phone: "" });
    };


    /* ========================
       UPDATE STATUS
    ======================== */
    const handleStatusChange = async (id, status) => {
        try {
            await updateLead(id, { status });
            fetchLeads();
        } catch {
            setError("Failed to update lead status");
        }
    };

    /* ========================
       DELETE LEAD
    ======================== */
    const handleDelete = async (id) => {
        if (!window.confirm("Delete this lead?")) return;

        try {
            await deleteLead(id);
            fetchLeads();
        } catch {
            setError("Failed to delete lead");
        }
    };

    /* ========================
       CONVERT LEAD
    ======================== */
    const handleConvert = async (id) => {
        if (!window.confirm("Convert lead to deal?")) return;

        try {
            await convertLead(id);
            fetchLeads();
        } catch {
            setError("Failed to convert lead");
        }
    };

    /* ========================
       UI
    ======================== */
    return (
        <>
            <Navbar />

            <div style={{ padding: "20px", maxWidth: "800px" }}>
                <h2>Leads</h2>

                {/* ERROR MESSAGE */}
                {error && (
                    <div
                        style={{
                            background: "#ffe5e5",
                            color: "#b00000",
                            padding: "10px",
                            marginBottom: "15px",
                            borderRadius: "4px",
                        }}
                    >
                        {error}
                    </div>
                )}

                {/* CREATE LEAD */}
                <div style={{ marginBottom: "20px" }}>
                    <input
                        name="name"
                        placeholder="Lead Name"
                        value={form.name}
                        onChange={handleChange}
                    />
                    <input
                        name="email"
                        placeholder="Email"
                        value={form.email}
                        onChange={handleChange}
                    />
                    <input
                        name="phone"
                        placeholder="Phone"
                        value={form.phone}
                        onChange={handleChange}
                    />

                    <button
                        onClick={addLead}
                        disabled={!form.name || !form.email || !form.phone}
                    >
                        Add Lead
                    </button>
                </div>

                {/* LEADS LIST */}
                <ul style={{ padding: 0 }}>
                    {leads.map((l) => (
                        <li
                            key={l.id}
                            style={{
                                border: "1px solid #ccc",
                                padding: "12px",
                                marginBottom: "10px",
                                listStyle: "none",
                                borderRadius: "4px",
                            }}
                        >
                            <strong>{l.name}</strong>
                            <br />
                            {l.email} | {l.phone}
                            <br />

                            {/* STATUS */}
                            Status:{" "}
                            <select
                                value={l.status}
                                onChange={(e) =>
                                    handleStatusChange(l.id, e.target.value)
                                }
                            >
                                <option value="new">New</option>
                                <option value="contacted">Contacted</option>
                                <option value="qualified">Qualified</option>
                                <option value="lost">Lost</option>
                            </select>

                            <br />

                            {/* CONVERT */}
                            {l.status === "qualified" && !l.is_converted && (
                                <button
                                    onClick={() => handleConvert(l.id)}
                                    style={{ marginTop: "6px" }}
                                >
                                    Convert to Deal
                                </button>
                            )}

                            {/* DELETE */}
                            <button
                                onClick={() => handleDelete(l.id)}
                                style={{
                                    marginLeft: "10px",
                                    color: "red",
                                }}
                            >
                                Delete
                            </button>
                        </li>
                    ))}
                </ul>
            </div>
        </>
    );
}
