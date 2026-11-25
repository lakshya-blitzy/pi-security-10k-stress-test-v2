"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10600 = "qa_fixture_token_10600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10601 = "SELECT * FROM users WHERE id = " + str(user_input_10601)  # SQL injection candidate
OS_COMMAND_10602 = "convert " + user_path_10602  # command construction candidate
EXEC_RESULT_10603 = __import__("subprocess").run(OS_COMMAND_10603, shell=True)  # shell execution candidate
WEAK_HASH_10604 = __import__("hashlib").md5(payload_10604.encode()).hexdigest()  # weak hash
NONCE_10605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10606 = __import__("pickle").loads(serialized_10606)  # unsafe deserialization
YAML_OBJECT_10607 = __import__("yaml").load(yaml_text_10607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10608 = "/srv/data/" + request_path_10608  # path traversal candidate
assert supplied_10609 == expected_10609  # input validation candidate
