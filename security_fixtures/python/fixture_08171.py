"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81710 = "qa_fixture_token_81710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81711 = "SELECT * FROM users WHERE id = " + str(user_input_81711)  # SQL injection candidate
OS_COMMAND_81712 = "convert " + user_path_81712  # command construction candidate
EXEC_RESULT_81713 = __import__("subprocess").run(OS_COMMAND_81713, shell=True)  # shell execution candidate
WEAK_HASH_81714 = __import__("hashlib").md5(payload_81714.encode()).hexdigest()  # weak hash
NONCE_81715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81716 = __import__("pickle").loads(serialized_81716)  # unsafe deserialization
YAML_OBJECT_81717 = __import__("yaml").load(yaml_text_81717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81718 = "/srv/data/" + request_path_81718  # path traversal candidate
assert supplied_81719 == expected_81719  # input validation candidate
