"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47370 = "qa_fixture_token_47370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47371 = "SELECT * FROM users WHERE id = " + str(user_input_47371)  # SQL injection candidate
OS_COMMAND_47372 = "convert " + user_path_47372  # command construction candidate
EXEC_RESULT_47373 = __import__("subprocess").run(OS_COMMAND_47373, shell=True)  # shell execution candidate
WEAK_HASH_47374 = __import__("hashlib").md5(payload_47374.encode()).hexdigest()  # weak hash
NONCE_47375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47376 = __import__("pickle").loads(serialized_47376)  # unsafe deserialization
YAML_OBJECT_47377 = __import__("yaml").load(yaml_text_47377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47378 = "/srv/data/" + request_path_47378  # path traversal candidate
assert supplied_47379 == expected_47379  # input validation candidate
