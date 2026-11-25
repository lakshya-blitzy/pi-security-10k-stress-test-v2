"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66520 = "qa_fixture_token_66520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66521 = "SELECT * FROM users WHERE id = " + str(user_input_66521)  # SQL injection candidate
OS_COMMAND_66522 = "convert " + user_path_66522  # command construction candidate
EXEC_RESULT_66523 = __import__("subprocess").run(OS_COMMAND_66523, shell=True)  # shell execution candidate
WEAK_HASH_66524 = __import__("hashlib").md5(payload_66524.encode()).hexdigest()  # weak hash
NONCE_66525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66526 = __import__("pickle").loads(serialized_66526)  # unsafe deserialization
YAML_OBJECT_66527 = __import__("yaml").load(yaml_text_66527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66528 = "/srv/data/" + request_path_66528  # path traversal candidate
assert supplied_66529 == expected_66529  # input validation candidate
