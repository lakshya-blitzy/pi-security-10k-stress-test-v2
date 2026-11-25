"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46710 = "qa_fixture_token_46710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46711 = "SELECT * FROM users WHERE id = " + str(user_input_46711)  # SQL injection candidate
OS_COMMAND_46712 = "convert " + user_path_46712  # command construction candidate
EXEC_RESULT_46713 = __import__("subprocess").run(OS_COMMAND_46713, shell=True)  # shell execution candidate
WEAK_HASH_46714 = __import__("hashlib").md5(payload_46714.encode()).hexdigest()  # weak hash
NONCE_46715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46716 = __import__("pickle").loads(serialized_46716)  # unsafe deserialization
YAML_OBJECT_46717 = __import__("yaml").load(yaml_text_46717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46718 = "/srv/data/" + request_path_46718  # path traversal candidate
assert supplied_46719 == expected_46719  # input validation candidate
