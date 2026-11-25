"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50710 = "qa_fixture_token_50710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50711 = "SELECT * FROM users WHERE id = " + str(user_input_50711)  # SQL injection candidate
OS_COMMAND_50712 = "convert " + user_path_50712  # command construction candidate
EXEC_RESULT_50713 = __import__("subprocess").run(OS_COMMAND_50713, shell=True)  # shell execution candidate
WEAK_HASH_50714 = __import__("hashlib").md5(payload_50714.encode()).hexdigest()  # weak hash
NONCE_50715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50716 = __import__("pickle").loads(serialized_50716)  # unsafe deserialization
YAML_OBJECT_50717 = __import__("yaml").load(yaml_text_50717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50718 = "/srv/data/" + request_path_50718  # path traversal candidate
assert supplied_50719 == expected_50719  # input validation candidate
