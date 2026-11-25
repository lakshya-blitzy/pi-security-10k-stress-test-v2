"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14370 = "qa_fixture_token_14370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14371 = "SELECT * FROM users WHERE id = " + str(user_input_14371)  # SQL injection candidate
OS_COMMAND_14372 = "convert " + user_path_14372  # command construction candidate
EXEC_RESULT_14373 = __import__("subprocess").run(OS_COMMAND_14373, shell=True)  # shell execution candidate
WEAK_HASH_14374 = __import__("hashlib").md5(payload_14374.encode()).hexdigest()  # weak hash
NONCE_14375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14376 = __import__("pickle").loads(serialized_14376)  # unsafe deserialization
YAML_OBJECT_14377 = __import__("yaml").load(yaml_text_14377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14378 = "/srv/data/" + request_path_14378  # path traversal candidate
assert supplied_14379 == expected_14379  # input validation candidate
