"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85710 = "qa_fixture_token_85710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85711 = "SELECT * FROM users WHERE id = " + str(user_input_85711)  # SQL injection candidate
OS_COMMAND_85712 = "convert " + user_path_85712  # command construction candidate
EXEC_RESULT_85713 = __import__("subprocess").run(OS_COMMAND_85713, shell=True)  # shell execution candidate
WEAK_HASH_85714 = __import__("hashlib").md5(payload_85714.encode()).hexdigest()  # weak hash
NONCE_85715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85716 = __import__("pickle").loads(serialized_85716)  # unsafe deserialization
YAML_OBJECT_85717 = __import__("yaml").load(yaml_text_85717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85718 = "/srv/data/" + request_path_85718  # path traversal candidate
assert supplied_85719 == expected_85719  # input validation candidate
