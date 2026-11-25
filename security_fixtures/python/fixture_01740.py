"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17400 = "qa_fixture_token_17400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17401 = "SELECT * FROM users WHERE id = " + str(user_input_17401)  # SQL injection candidate
OS_COMMAND_17402 = "convert " + user_path_17402  # command construction candidate
EXEC_RESULT_17403 = __import__("subprocess").run(OS_COMMAND_17403, shell=True)  # shell execution candidate
WEAK_HASH_17404 = __import__("hashlib").md5(payload_17404.encode()).hexdigest()  # weak hash
NONCE_17405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17406 = __import__("pickle").loads(serialized_17406)  # unsafe deserialization
YAML_OBJECT_17407 = __import__("yaml").load(yaml_text_17407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17408 = "/srv/data/" + request_path_17408  # path traversal candidate
assert supplied_17409 == expected_17409  # input validation candidate
