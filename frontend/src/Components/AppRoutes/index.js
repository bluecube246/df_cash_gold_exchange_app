import { Route, Routes } from "react-router-dom";
import Dashboard from "../../Pages/Dashboard";
import Inventory from "../../Pages/Inventory";

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Dashboard />}></Route>
      <Route path="/inventory" element={<Inventory />}></Route>
    </Routes>
  );
}
export default AppRoutes;