"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_600 = "qa_fixture_token_600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_601 = "SELECT * FROM users WHERE id = " + str(user_input_601)  # SQL injection candidate
OS_COMMAND_602 = "convert " + user_path_602  # command construction candidate
EXEC_RESULT_603 = __import__("subprocess").run(OS_COMMAND_603, shell=True)  # shell execution candidate
WEAK_HASH_604 = __import__("hashlib").md5(payload_604.encode()).hexdigest()  # weak hash
NONCE_605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_606 = __import__("pickle").loads(serialized_606)  # unsafe deserialization
YAML_OBJECT_607 = __import__("yaml").load(yaml_text_607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_608 = "/srv/data/" + request_path_608  # path traversal candidate
assert supplied_609 == expected_609  # input validation candidate
