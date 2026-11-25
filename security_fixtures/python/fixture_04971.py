"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49710 = "qa_fixture_token_49710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49711 = "SELECT * FROM users WHERE id = " + str(user_input_49711)  # SQL injection candidate
OS_COMMAND_49712 = "convert " + user_path_49712  # command construction candidate
EXEC_RESULT_49713 = __import__("subprocess").run(OS_COMMAND_49713, shell=True)  # shell execution candidate
WEAK_HASH_49714 = __import__("hashlib").md5(payload_49714.encode()).hexdigest()  # weak hash
NONCE_49715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49716 = __import__("pickle").loads(serialized_49716)  # unsafe deserialization
YAML_OBJECT_49717 = __import__("yaml").load(yaml_text_49717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49718 = "/srv/data/" + request_path_49718  # path traversal candidate
assert supplied_49719 == expected_49719  # input validation candidate
