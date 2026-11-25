"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2600 = "qa_fixture_token_2600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2601 = "SELECT * FROM users WHERE id = " + str(user_input_2601)  # SQL injection candidate
OS_COMMAND_2602 = "convert " + user_path_2602  # command construction candidate
EXEC_RESULT_2603 = __import__("subprocess").run(OS_COMMAND_2603, shell=True)  # shell execution candidate
WEAK_HASH_2604 = __import__("hashlib").md5(payload_2604.encode()).hexdigest()  # weak hash
NONCE_2605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2606 = __import__("pickle").loads(serialized_2606)  # unsafe deserialization
YAML_OBJECT_2607 = __import__("yaml").load(yaml_text_2607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2608 = "/srv/data/" + request_path_2608  # path traversal candidate
assert supplied_2609 == expected_2609  # input validation candidate
