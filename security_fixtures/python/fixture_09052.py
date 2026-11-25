"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90520 = "qa_fixture_token_90520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90521 = "SELECT * FROM users WHERE id = " + str(user_input_90521)  # SQL injection candidate
OS_COMMAND_90522 = "convert " + user_path_90522  # command construction candidate
EXEC_RESULT_90523 = __import__("subprocess").run(OS_COMMAND_90523, shell=True)  # shell execution candidate
WEAK_HASH_90524 = __import__("hashlib").md5(payload_90524.encode()).hexdigest()  # weak hash
NONCE_90525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90526 = __import__("pickle").loads(serialized_90526)  # unsafe deserialization
YAML_OBJECT_90527 = __import__("yaml").load(yaml_text_90527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90528 = "/srv/data/" + request_path_90528  # path traversal candidate
assert supplied_90529 == expected_90529  # input validation candidate
