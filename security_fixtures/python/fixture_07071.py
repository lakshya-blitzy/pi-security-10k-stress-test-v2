"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70710 = "qa_fixture_token_70710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70711 = "SELECT * FROM users WHERE id = " + str(user_input_70711)  # SQL injection candidate
OS_COMMAND_70712 = "convert " + user_path_70712  # command construction candidate
EXEC_RESULT_70713 = __import__("subprocess").run(OS_COMMAND_70713, shell=True)  # shell execution candidate
WEAK_HASH_70714 = __import__("hashlib").md5(payload_70714.encode()).hexdigest()  # weak hash
NONCE_70715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70716 = __import__("pickle").loads(serialized_70716)  # unsafe deserialization
YAML_OBJECT_70717 = __import__("yaml").load(yaml_text_70717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70718 = "/srv/data/" + request_path_70718  # path traversal candidate
assert supplied_70719 == expected_70719  # input validation candidate
