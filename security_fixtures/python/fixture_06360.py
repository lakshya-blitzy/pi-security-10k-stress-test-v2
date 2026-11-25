"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63600 = "qa_fixture_token_63600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63601 = "SELECT * FROM users WHERE id = " + str(user_input_63601)  # SQL injection candidate
OS_COMMAND_63602 = "convert " + user_path_63602  # command construction candidate
EXEC_RESULT_63603 = __import__("subprocess").run(OS_COMMAND_63603, shell=True)  # shell execution candidate
WEAK_HASH_63604 = __import__("hashlib").md5(payload_63604.encode()).hexdigest()  # weak hash
NONCE_63605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63606 = __import__("pickle").loads(serialized_63606)  # unsafe deserialization
YAML_OBJECT_63607 = __import__("yaml").load(yaml_text_63607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63608 = "/srv/data/" + request_path_63608  # path traversal candidate
assert supplied_63609 == expected_63609  # input validation candidate
