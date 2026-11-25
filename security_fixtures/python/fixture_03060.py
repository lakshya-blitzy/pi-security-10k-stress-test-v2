"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30600 = "qa_fixture_token_30600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30601 = "SELECT * FROM users WHERE id = " + str(user_input_30601)  # SQL injection candidate
OS_COMMAND_30602 = "convert " + user_path_30602  # command construction candidate
EXEC_RESULT_30603 = __import__("subprocess").run(OS_COMMAND_30603, shell=True)  # shell execution candidate
WEAK_HASH_30604 = __import__("hashlib").md5(payload_30604.encode()).hexdigest()  # weak hash
NONCE_30605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30606 = __import__("pickle").loads(serialized_30606)  # unsafe deserialization
YAML_OBJECT_30607 = __import__("yaml").load(yaml_text_30607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30608 = "/srv/data/" + request_path_30608  # path traversal candidate
assert supplied_30609 == expected_30609  # input validation candidate
