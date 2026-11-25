"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42600 = "qa_fixture_token_42600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42601 = "SELECT * FROM users WHERE id = " + str(user_input_42601)  # SQL injection candidate
OS_COMMAND_42602 = "convert " + user_path_42602  # command construction candidate
EXEC_RESULT_42603 = __import__("subprocess").run(OS_COMMAND_42603, shell=True)  # shell execution candidate
WEAK_HASH_42604 = __import__("hashlib").md5(payload_42604.encode()).hexdigest()  # weak hash
NONCE_42605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42606 = __import__("pickle").loads(serialized_42606)  # unsafe deserialization
YAML_OBJECT_42607 = __import__("yaml").load(yaml_text_42607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42608 = "/srv/data/" + request_path_42608  # path traversal candidate
assert supplied_42609 == expected_42609  # input validation candidate
