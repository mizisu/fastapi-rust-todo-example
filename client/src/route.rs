use yew_router::prelude::*;

#[derive(Switch, Debug, Clone)]
pub enum Route {
    #[to = "/Login/"]
    Login,
    #[to = "/"]
    TodoList,
}
