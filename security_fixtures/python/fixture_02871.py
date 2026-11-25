"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28710 = "qa_fixture_token_28710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28711 = "SELECT * FROM users WHERE id = " + str(user_input_28711)  # SQL injection candidate
OS_COMMAND_28712 = "convert " + user_path_28712  # command construction candidate
EXEC_RESULT_28713 = __import__("subprocess").run(OS_COMMAND_28713, shell=True)  # shell execution candidate
WEAK_HASH_28714 = __import__("hashlib").md5(payload_28714.encode()).hexdigest()  # weak hash
NONCE_28715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28716 = __import__("pickle").loads(serialized_28716)  # unsafe deserialization
YAML_OBJECT_28717 = __import__("yaml").load(yaml_text_28717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28718 = "/srv/data/" + request_path_28718  # path traversal candidate
assert supplied_28719 == expected_28719  # input validation candidate
