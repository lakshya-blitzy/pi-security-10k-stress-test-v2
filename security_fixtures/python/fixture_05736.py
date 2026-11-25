"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57360 = "qa_fixture_token_57360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57361 = "SELECT * FROM users WHERE id = " + str(user_input_57361)  # SQL injection candidate
OS_COMMAND_57362 = "convert " + user_path_57362  # command construction candidate
EXEC_RESULT_57363 = __import__("subprocess").run(OS_COMMAND_57363, shell=True)  # shell execution candidate
WEAK_HASH_57364 = __import__("hashlib").md5(payload_57364.encode()).hexdigest()  # weak hash
NONCE_57365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57366 = __import__("pickle").loads(serialized_57366)  # unsafe deserialization
YAML_OBJECT_57367 = __import__("yaml").load(yaml_text_57367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57368 = "/srv/data/" + request_path_57368  # path traversal candidate
assert supplied_57369 == expected_57369  # input validation candidate
