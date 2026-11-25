"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15710 = "qa_fixture_token_15710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15711 = "SELECT * FROM users WHERE id = " + str(user_input_15711)  # SQL injection candidate
OS_COMMAND_15712 = "convert " + user_path_15712  # command construction candidate
EXEC_RESULT_15713 = __import__("subprocess").run(OS_COMMAND_15713, shell=True)  # shell execution candidate
WEAK_HASH_15714 = __import__("hashlib").md5(payload_15714.encode()).hexdigest()  # weak hash
NONCE_15715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15716 = __import__("pickle").loads(serialized_15716)  # unsafe deserialization
YAML_OBJECT_15717 = __import__("yaml").load(yaml_text_15717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15718 = "/srv/data/" + request_path_15718  # path traversal candidate
assert supplied_15719 == expected_15719  # input validation candidate
