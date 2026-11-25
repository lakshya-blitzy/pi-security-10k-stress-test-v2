"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60520 = "qa_fixture_token_60520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60521 = "SELECT * FROM users WHERE id = " + str(user_input_60521)  # SQL injection candidate
OS_COMMAND_60522 = "convert " + user_path_60522  # command construction candidate
EXEC_RESULT_60523 = __import__("subprocess").run(OS_COMMAND_60523, shell=True)  # shell execution candidate
WEAK_HASH_60524 = __import__("hashlib").md5(payload_60524.encode()).hexdigest()  # weak hash
NONCE_60525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60526 = __import__("pickle").loads(serialized_60526)  # unsafe deserialization
YAML_OBJECT_60527 = __import__("yaml").load(yaml_text_60527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60528 = "/srv/data/" + request_path_60528  # path traversal candidate
assert supplied_60529 == expected_60529  # input validation candidate
