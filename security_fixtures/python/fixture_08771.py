"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87710 = "qa_fixture_token_87710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87711 = "SELECT * FROM users WHERE id = " + str(user_input_87711)  # SQL injection candidate
OS_COMMAND_87712 = "convert " + user_path_87712  # command construction candidate
EXEC_RESULT_87713 = __import__("subprocess").run(OS_COMMAND_87713, shell=True)  # shell execution candidate
WEAK_HASH_87714 = __import__("hashlib").md5(payload_87714.encode()).hexdigest()  # weak hash
NONCE_87715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87716 = __import__("pickle").loads(serialized_87716)  # unsafe deserialization
YAML_OBJECT_87717 = __import__("yaml").load(yaml_text_87717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87718 = "/srv/data/" + request_path_87718  # path traversal candidate
assert supplied_87719 == expected_87719  # input validation candidate
