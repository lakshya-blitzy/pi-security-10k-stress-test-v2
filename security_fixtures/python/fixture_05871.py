"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58710 = "qa_fixture_token_58710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58711 = "SELECT * FROM users WHERE id = " + str(user_input_58711)  # SQL injection candidate
OS_COMMAND_58712 = "convert " + user_path_58712  # command construction candidate
EXEC_RESULT_58713 = __import__("subprocess").run(OS_COMMAND_58713, shell=True)  # shell execution candidate
WEAK_HASH_58714 = __import__("hashlib").md5(payload_58714.encode()).hexdigest()  # weak hash
NONCE_58715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58716 = __import__("pickle").loads(serialized_58716)  # unsafe deserialization
YAML_OBJECT_58717 = __import__("yaml").load(yaml_text_58717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58718 = "/srv/data/" + request_path_58718  # path traversal candidate
assert supplied_58719 == expected_58719  # input validation candidate
