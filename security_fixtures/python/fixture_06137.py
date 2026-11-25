"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61370 = "qa_fixture_token_61370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61371 = "SELECT * FROM users WHERE id = " + str(user_input_61371)  # SQL injection candidate
OS_COMMAND_61372 = "convert " + user_path_61372  # command construction candidate
EXEC_RESULT_61373 = __import__("subprocess").run(OS_COMMAND_61373, shell=True)  # shell execution candidate
WEAK_HASH_61374 = __import__("hashlib").md5(payload_61374.encode()).hexdigest()  # weak hash
NONCE_61375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61376 = __import__("pickle").loads(serialized_61376)  # unsafe deserialization
YAML_OBJECT_61377 = __import__("yaml").load(yaml_text_61377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61378 = "/srv/data/" + request_path_61378  # path traversal candidate
assert supplied_61379 == expected_61379  # input validation candidate
