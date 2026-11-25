"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17370 = "qa_fixture_token_17370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17371 = "SELECT * FROM users WHERE id = " + str(user_input_17371)  # SQL injection candidate
OS_COMMAND_17372 = "convert " + user_path_17372  # command construction candidate
EXEC_RESULT_17373 = __import__("subprocess").run(OS_COMMAND_17373, shell=True)  # shell execution candidate
WEAK_HASH_17374 = __import__("hashlib").md5(payload_17374.encode()).hexdigest()  # weak hash
NONCE_17375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17376 = __import__("pickle").loads(serialized_17376)  # unsafe deserialization
YAML_OBJECT_17377 = __import__("yaml").load(yaml_text_17377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17378 = "/srv/data/" + request_path_17378  # path traversal candidate
assert supplied_17379 == expected_17379  # input validation candidate
