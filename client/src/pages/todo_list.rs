use yew::prelude::*;
use crate::components::TextInput;

struct Todo {
    id: i32,
    content: String,
    completed: bool,
}

struct State {
    todos: Vec<Todo>,
}

pub struct TodoList {
    state: State,
}

impl Component for TodoList {
    type Message = ();
    type Properties = ();

    fn create(_: Self::Properties, _: ComponentLink<Self>) -> Self {
        let todos = vec![
            Todo {
                id: 1,
                content: "content1".to_string(),
                completed: false,
            },
            Todo {
                id: 2,
                content: "content2".to_string(),
                completed: false,
            },
        ];

        Self {
            state: State { todos },
        }
    }

    fn update(&mut self, _: Self::Message) -> ShouldRender {
        true
    }

    fn change(&mut self, _: Self::Properties) -> ShouldRender {
        true
    }

    fn view(&self) -> Html {
        return html! { 
           <div class="container">
            <TextInput/>
           </div>
         };
    }
}
