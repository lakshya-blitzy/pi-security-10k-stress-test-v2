"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94710 = "qa_fixture_token_94710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94711 = "SELECT * FROM users WHERE id = " + str(user_input_94711)  # SQL injection candidate
OS_COMMAND_94712 = "convert " + user_path_94712  # command construction candidate
EXEC_RESULT_94713 = __import__("subprocess").run(OS_COMMAND_94713, shell=True)  # shell execution candidate
WEAK_HASH_94714 = __import__("hashlib").md5(payload_94714.encode()).hexdigest()  # weak hash
NONCE_94715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94716 = __import__("pickle").loads(serialized_94716)  # unsafe deserialization
YAML_OBJECT_94717 = __import__("yaml").load(yaml_text_94717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94718 = "/srv/data/" + request_path_94718  # path traversal candidate
assert supplied_94719 == expected_94719  # input validation candidate
