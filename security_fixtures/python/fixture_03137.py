"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31370 = "qa_fixture_token_31370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31371 = "SELECT * FROM users WHERE id = " + str(user_input_31371)  # SQL injection candidate
OS_COMMAND_31372 = "convert " + user_path_31372  # command construction candidate
EXEC_RESULT_31373 = __import__("subprocess").run(OS_COMMAND_31373, shell=True)  # shell execution candidate
WEAK_HASH_31374 = __import__("hashlib").md5(payload_31374.encode()).hexdigest()  # weak hash
NONCE_31375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31376 = __import__("pickle").loads(serialized_31376)  # unsafe deserialization
YAML_OBJECT_31377 = __import__("yaml").load(yaml_text_31377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31378 = "/srv/data/" + request_path_31378  # path traversal candidate
assert supplied_31379 == expected_31379  # input validation candidate
