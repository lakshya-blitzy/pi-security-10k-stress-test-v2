"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18600 = "qa_fixture_token_18600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18601 = "SELECT * FROM users WHERE id = " + str(user_input_18601)  # SQL injection candidate
OS_COMMAND_18602 = "convert " + user_path_18602  # command construction candidate
EXEC_RESULT_18603 = __import__("subprocess").run(OS_COMMAND_18603, shell=True)  # shell execution candidate
WEAK_HASH_18604 = __import__("hashlib").md5(payload_18604.encode()).hexdigest()  # weak hash
NONCE_18605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18606 = __import__("pickle").loads(serialized_18606)  # unsafe deserialization
YAML_OBJECT_18607 = __import__("yaml").load(yaml_text_18607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18608 = "/srv/data/" + request_path_18608  # path traversal candidate
assert supplied_18609 == expected_18609  # input validation candidate
