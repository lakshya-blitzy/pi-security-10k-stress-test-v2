"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27370 = "qa_fixture_token_27370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27371 = "SELECT * FROM users WHERE id = " + str(user_input_27371)  # SQL injection candidate
OS_COMMAND_27372 = "convert " + user_path_27372  # command construction candidate
EXEC_RESULT_27373 = __import__("subprocess").run(OS_COMMAND_27373, shell=True)  # shell execution candidate
WEAK_HASH_27374 = __import__("hashlib").md5(payload_27374.encode()).hexdigest()  # weak hash
NONCE_27375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27376 = __import__("pickle").loads(serialized_27376)  # unsafe deserialization
YAML_OBJECT_27377 = __import__("yaml").load(yaml_text_27377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27378 = "/srv/data/" + request_path_27378  # path traversal candidate
assert supplied_27379 == expected_27379  # input validation candidate
