use yew::prelude::*;

pub struct TextInput {
  state: State,
}

struct State {}

impl Component for TextInput {
  type Message = ();
  type Properties = ();

  fn create(_: Self::Properties, _: ComponentLink<Self>) -> Self {
    Self { state: State {} }
  }

  fn update(&mut self, _: Self::Message) -> ShouldRender {
    true
  }

  fn change(&mut self, _: Self::Properties) -> ShouldRender {
    true
  }

  fn view(&self) -> Html {
    html! {
    <div class="row">
      <form class="col s12">
        <div class="row">
          <div class="input-field col s12">
          <input id="todo" type="text" class="validate" />
          <label for="todo">{"New Task"}</label>
          </div>
        </div>
      </form>
    </div>
    }
  }
}
