use yew::prelude::*;
use yew::events::{Event, InputData};
use yew::services::ConsoleService;

pub enum Msg {
  Submit,
  ValueUpdate(String),
}

pub struct TextInput {
  state: State,
  link: ComponentLink<Self>,
}

struct State {
  value: String,
}

impl Component for TextInput {
  type Message = Msg;
  type Properties = ();

  fn create(_: Self::Properties, link: ComponentLink<Self>) -> Self {
    Self { state: State {
      value: "".to_string(),
    }, link }
  }

  fn update(&mut self, msg: Self::Message) -> ShouldRender {
    match msg {
      Msg::Submit => {
        println!("Submit!")
      },
      Msg::ValueUpdate(value) => {
        self.state.value = value;
      }
    }

    true
  }

  fn change(&mut self, _: Self::Properties) -> ShouldRender {
    true
  }

  fn view(&self) -> Html {
    let onsubmit = self.link.callback(|e: FocusEvent|{
      e.prevent_default();
      Msg::Submit
    });

    html! {
    <div class="row">
      <form class="col s12" onsubmit=onsubmit>
        <div class="row">
          <div class="input-field col s12">
          <input id="todo" type="text" class="validate" 
                 value=&self.state.value
                 oninput=self.link.callback(|e : InputData| Msg::ValueUpdate(e.value))
           />
          <label for="todo">{"New Task"}</label>
          </div>
        </div>
      </form>
    </div>
    }
  }
}
