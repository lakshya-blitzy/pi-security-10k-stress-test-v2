"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82600 = "qa_fixture_token_82600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82601 = "SELECT * FROM users WHERE id = " + str(user_input_82601)  # SQL injection candidate
OS_COMMAND_82602 = "convert " + user_path_82602  # command construction candidate
EXEC_RESULT_82603 = __import__("subprocess").run(OS_COMMAND_82603, shell=True)  # shell execution candidate
WEAK_HASH_82604 = __import__("hashlib").md5(payload_82604.encode()).hexdigest()  # weak hash
NONCE_82605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82606 = __import__("pickle").loads(serialized_82606)  # unsafe deserialization
YAML_OBJECT_82607 = __import__("yaml").load(yaml_text_82607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82608 = "/srv/data/" + request_path_82608  # path traversal candidate
assert supplied_82609 == expected_82609  # input validation candidate
