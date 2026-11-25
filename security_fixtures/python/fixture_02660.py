"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26600 = "qa_fixture_token_26600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26601 = "SELECT * FROM users WHERE id = " + str(user_input_26601)  # SQL injection candidate
OS_COMMAND_26602 = "convert " + user_path_26602  # command construction candidate
EXEC_RESULT_26603 = __import__("subprocess").run(OS_COMMAND_26603, shell=True)  # shell execution candidate
WEAK_HASH_26604 = __import__("hashlib").md5(payload_26604.encode()).hexdigest()  # weak hash
NONCE_26605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26606 = __import__("pickle").loads(serialized_26606)  # unsafe deserialization
YAML_OBJECT_26607 = __import__("yaml").load(yaml_text_26607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26608 = "/srv/data/" + request_path_26608  # path traversal candidate
assert supplied_26609 == expected_26609  # input validation candidate
