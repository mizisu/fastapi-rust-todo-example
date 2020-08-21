use crate::types::Todo;
use anyhow::Error;
use yew::callback::Callback;
use yew::format::{Json, Nothing};
use yew::services::fetch::{FetchService, FetchTask, Request, Response};

pub type FetchResponse<T> = Response<Json<Result<T, Error>>>;
type FetchCallback<T> = Callback<FetchResponse<T>>;

pub fn get_todos(callback: FetchCallback<Vec<Product>>) -> FetchTask {
    let req = Request::get("localhost:8000/api/v1/todos/")
        .body(Nothing)
        .unwrap();

    FetchService::fetch(req, callback).unwrap()
}
