"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69600 = "qa_fixture_token_69600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69601 = "SELECT * FROM users WHERE id = " + str(user_input_69601)  # SQL injection candidate
OS_COMMAND_69602 = "convert " + user_path_69602  # command construction candidate
EXEC_RESULT_69603 = __import__("subprocess").run(OS_COMMAND_69603, shell=True)  # shell execution candidate
WEAK_HASH_69604 = __import__("hashlib").md5(payload_69604.encode()).hexdigest()  # weak hash
NONCE_69605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69606 = __import__("pickle").loads(serialized_69606)  # unsafe deserialization
YAML_OBJECT_69607 = __import__("yaml").load(yaml_text_69607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69608 = "/srv/data/" + request_path_69608  # path traversal candidate
assert supplied_69609 == expected_69609  # input validation candidate
