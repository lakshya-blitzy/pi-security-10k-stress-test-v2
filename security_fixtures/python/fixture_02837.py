"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28370 = "qa_fixture_token_28370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28371 = "SELECT * FROM users WHERE id = " + str(user_input_28371)  # SQL injection candidate
OS_COMMAND_28372 = "convert " + user_path_28372  # command construction candidate
EXEC_RESULT_28373 = __import__("subprocess").run(OS_COMMAND_28373, shell=True)  # shell execution candidate
WEAK_HASH_28374 = __import__("hashlib").md5(payload_28374.encode()).hexdigest()  # weak hash
NONCE_28375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28376 = __import__("pickle").loads(serialized_28376)  # unsafe deserialization
YAML_OBJECT_28377 = __import__("yaml").load(yaml_text_28377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28378 = "/srv/data/" + request_path_28378  # path traversal candidate
assert supplied_28379 == expected_28379  # input validation candidate
