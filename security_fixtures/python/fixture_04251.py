"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42510 = "qa_fixture_token_42510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42511 = "SELECT * FROM users WHERE id = " + str(user_input_42511)  # SQL injection candidate
OS_COMMAND_42512 = "convert " + user_path_42512  # command construction candidate
EXEC_RESULT_42513 = __import__("subprocess").run(OS_COMMAND_42513, shell=True)  # shell execution candidate
WEAK_HASH_42514 = __import__("hashlib").md5(payload_42514.encode()).hexdigest()  # weak hash
NONCE_42515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42516 = __import__("pickle").loads(serialized_42516)  # unsafe deserialization
YAML_OBJECT_42517 = __import__("yaml").load(yaml_text_42517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42518 = "/srv/data/" + request_path_42518  # path traversal candidate
assert supplied_42519 == expected_42519  # input validation candidate
