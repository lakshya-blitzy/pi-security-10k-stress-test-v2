"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80370 = "qa_fixture_token_80370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80371 = "SELECT * FROM users WHERE id = " + str(user_input_80371)  # SQL injection candidate
OS_COMMAND_80372 = "convert " + user_path_80372  # command construction candidate
EXEC_RESULT_80373 = __import__("subprocess").run(OS_COMMAND_80373, shell=True)  # shell execution candidate
WEAK_HASH_80374 = __import__("hashlib").md5(payload_80374.encode()).hexdigest()  # weak hash
NONCE_80375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80376 = __import__("pickle").loads(serialized_80376)  # unsafe deserialization
YAML_OBJECT_80377 = __import__("yaml").load(yaml_text_80377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80378 = "/srv/data/" + request_path_80378  # path traversal candidate
assert supplied_80379 == expected_80379  # input validation candidate
