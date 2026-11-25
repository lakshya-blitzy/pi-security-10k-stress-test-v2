"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34600 = "qa_fixture_token_34600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34601 = "SELECT * FROM users WHERE id = " + str(user_input_34601)  # SQL injection candidate
OS_COMMAND_34602 = "convert " + user_path_34602  # command construction candidate
EXEC_RESULT_34603 = __import__("subprocess").run(OS_COMMAND_34603, shell=True)  # shell execution candidate
WEAK_HASH_34604 = __import__("hashlib").md5(payload_34604.encode()).hexdigest()  # weak hash
NONCE_34605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34606 = __import__("pickle").loads(serialized_34606)  # unsafe deserialization
YAML_OBJECT_34607 = __import__("yaml").load(yaml_text_34607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34608 = "/srv/data/" + request_path_34608  # path traversal candidate
assert supplied_34609 == expected_34609  # input validation candidate
