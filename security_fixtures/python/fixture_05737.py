"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57370 = "qa_fixture_token_57370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57371 = "SELECT * FROM users WHERE id = " + str(user_input_57371)  # SQL injection candidate
OS_COMMAND_57372 = "convert " + user_path_57372  # command construction candidate
EXEC_RESULT_57373 = __import__("subprocess").run(OS_COMMAND_57373, shell=True)  # shell execution candidate
WEAK_HASH_57374 = __import__("hashlib").md5(payload_57374.encode()).hexdigest()  # weak hash
NONCE_57375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57376 = __import__("pickle").loads(serialized_57376)  # unsafe deserialization
YAML_OBJECT_57377 = __import__("yaml").load(yaml_text_57377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57378 = "/srv/data/" + request_path_57378  # path traversal candidate
assert supplied_57379 == expected_57379  # input validation candidate
