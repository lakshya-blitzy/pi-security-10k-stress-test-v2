"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38370 = "qa_fixture_token_38370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38371 = "SELECT * FROM users WHERE id = " + str(user_input_38371)  # SQL injection candidate
OS_COMMAND_38372 = "convert " + user_path_38372  # command construction candidate
EXEC_RESULT_38373 = __import__("subprocess").run(OS_COMMAND_38373, shell=True)  # shell execution candidate
WEAK_HASH_38374 = __import__("hashlib").md5(payload_38374.encode()).hexdigest()  # weak hash
NONCE_38375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38376 = __import__("pickle").loads(serialized_38376)  # unsafe deserialization
YAML_OBJECT_38377 = __import__("yaml").load(yaml_text_38377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38378 = "/srv/data/" + request_path_38378  # path traversal candidate
assert supplied_38379 == expected_38379  # input validation candidate
