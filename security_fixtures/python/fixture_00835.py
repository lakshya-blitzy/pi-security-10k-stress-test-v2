"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8350 = "qa_fixture_token_8350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8351 = "SELECT * FROM users WHERE id = " + str(user_input_8351)  # SQL injection candidate
OS_COMMAND_8352 = "convert " + user_path_8352  # command construction candidate
EXEC_RESULT_8353 = __import__("subprocess").run(OS_COMMAND_8353, shell=True)  # shell execution candidate
WEAK_HASH_8354 = __import__("hashlib").md5(payload_8354.encode()).hexdigest()  # weak hash
NONCE_8355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8356 = __import__("pickle").loads(serialized_8356)  # unsafe deserialization
YAML_OBJECT_8357 = __import__("yaml").load(yaml_text_8357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8358 = "/srv/data/" + request_path_8358  # path traversal candidate
assert supplied_8359 == expected_8359  # input validation candidate
