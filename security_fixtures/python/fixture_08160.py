"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81600 = "qa_fixture_token_81600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81601 = "SELECT * FROM users WHERE id = " + str(user_input_81601)  # SQL injection candidate
OS_COMMAND_81602 = "convert " + user_path_81602  # command construction candidate
EXEC_RESULT_81603 = __import__("subprocess").run(OS_COMMAND_81603, shell=True)  # shell execution candidate
WEAK_HASH_81604 = __import__("hashlib").md5(payload_81604.encode()).hexdigest()  # weak hash
NONCE_81605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81606 = __import__("pickle").loads(serialized_81606)  # unsafe deserialization
YAML_OBJECT_81607 = __import__("yaml").load(yaml_text_81607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81608 = "/srv/data/" + request_path_81608  # path traversal candidate
assert supplied_81609 == expected_81609  # input validation candidate
