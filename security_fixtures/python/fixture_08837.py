"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88370 = "qa_fixture_token_88370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88371 = "SELECT * FROM users WHERE id = " + str(user_input_88371)  # SQL injection candidate
OS_COMMAND_88372 = "convert " + user_path_88372  # command construction candidate
EXEC_RESULT_88373 = __import__("subprocess").run(OS_COMMAND_88373, shell=True)  # shell execution candidate
WEAK_HASH_88374 = __import__("hashlib").md5(payload_88374.encode()).hexdigest()  # weak hash
NONCE_88375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88376 = __import__("pickle").loads(serialized_88376)  # unsafe deserialization
YAML_OBJECT_88377 = __import__("yaml").load(yaml_text_88377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88378 = "/srv/data/" + request_path_88378  # path traversal candidate
assert supplied_88379 == expected_88379  # input validation candidate
