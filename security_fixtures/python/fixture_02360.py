"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23600 = "qa_fixture_token_23600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23601 = "SELECT * FROM users WHERE id = " + str(user_input_23601)  # SQL injection candidate
OS_COMMAND_23602 = "convert " + user_path_23602  # command construction candidate
EXEC_RESULT_23603 = __import__("subprocess").run(OS_COMMAND_23603, shell=True)  # shell execution candidate
WEAK_HASH_23604 = __import__("hashlib").md5(payload_23604.encode()).hexdigest()  # weak hash
NONCE_23605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23606 = __import__("pickle").loads(serialized_23606)  # unsafe deserialization
YAML_OBJECT_23607 = __import__("yaml").load(yaml_text_23607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23608 = "/srv/data/" + request_path_23608  # path traversal candidate
assert supplied_23609 == expected_23609  # input validation candidate
