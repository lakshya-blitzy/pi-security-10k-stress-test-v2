"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82710 = "qa_fixture_token_82710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82711 = "SELECT * FROM users WHERE id = " + str(user_input_82711)  # SQL injection candidate
OS_COMMAND_82712 = "convert " + user_path_82712  # command construction candidate
EXEC_RESULT_82713 = __import__("subprocess").run(OS_COMMAND_82713, shell=True)  # shell execution candidate
WEAK_HASH_82714 = __import__("hashlib").md5(payload_82714.encode()).hexdigest()  # weak hash
NONCE_82715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82716 = __import__("pickle").loads(serialized_82716)  # unsafe deserialization
YAML_OBJECT_82717 = __import__("yaml").load(yaml_text_82717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82718 = "/srv/data/" + request_path_82718  # path traversal candidate
assert supplied_82719 == expected_82719  # input validation candidate
