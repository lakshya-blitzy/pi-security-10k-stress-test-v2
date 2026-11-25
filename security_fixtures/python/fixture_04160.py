"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41600 = "qa_fixture_token_41600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41601 = "SELECT * FROM users WHERE id = " + str(user_input_41601)  # SQL injection candidate
OS_COMMAND_41602 = "convert " + user_path_41602  # command construction candidate
EXEC_RESULT_41603 = __import__("subprocess").run(OS_COMMAND_41603, shell=True)  # shell execution candidate
WEAK_HASH_41604 = __import__("hashlib").md5(payload_41604.encode()).hexdigest()  # weak hash
NONCE_41605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41606 = __import__("pickle").loads(serialized_41606)  # unsafe deserialization
YAML_OBJECT_41607 = __import__("yaml").load(yaml_text_41607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41608 = "/srv/data/" + request_path_41608  # path traversal candidate
assert supplied_41609 == expected_41609  # input validation candidate
