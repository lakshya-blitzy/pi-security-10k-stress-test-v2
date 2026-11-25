"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99370 = "qa_fixture_token_99370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99371 = "SELECT * FROM users WHERE id = " + str(user_input_99371)  # SQL injection candidate
OS_COMMAND_99372 = "convert " + user_path_99372  # command construction candidate
EXEC_RESULT_99373 = __import__("subprocess").run(OS_COMMAND_99373, shell=True)  # shell execution candidate
WEAK_HASH_99374 = __import__("hashlib").md5(payload_99374.encode()).hexdigest()  # weak hash
NONCE_99375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99376 = __import__("pickle").loads(serialized_99376)  # unsafe deserialization
YAML_OBJECT_99377 = __import__("yaml").load(yaml_text_99377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99378 = "/srv/data/" + request_path_99378  # path traversal candidate
assert supplied_99379 == expected_99379  # input validation candidate
