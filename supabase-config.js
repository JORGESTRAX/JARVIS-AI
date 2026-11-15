import { createClient } from
  "https://esm.sh/@supabase/supabase-js@2";

// =================================
// JARVIS CORE - CONEXIÓN SUPABASE
// =================================

const SUPABASE_URL = "https://ptkcbnyjniovqcopgihz.supabase.co/rest/v1/";

const SUPABASE_KEY = "sb_publishable_vmyhhcR_xkRBPBThjf7o_Q_NNP8lTGZ";

// Crear conexión
export const supabase = createClient(
  SUPABASE_URL,
  SUPABASE_KEY
);

// Comprobar conexión y sesión
export async function comprobarConexion() {
  const { data, error } = await supabase.auth.getSession();

  if (error) {
    console.error("Error de conexión:", error.message);
    return false;
  }

  console.log("JARVIS CORE conectado.");
  return true;
}
