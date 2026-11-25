"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71710 = "qa_fixture_token_71710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71711 = "SELECT * FROM users WHERE id = " + str(user_input_71711)  # SQL injection candidate
OS_COMMAND_71712 = "convert " + user_path_71712  # command construction candidate
EXEC_RESULT_71713 = __import__("subprocess").run(OS_COMMAND_71713, shell=True)  # shell execution candidate
WEAK_HASH_71714 = __import__("hashlib").md5(payload_71714.encode()).hexdigest()  # weak hash
NONCE_71715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71716 = __import__("pickle").loads(serialized_71716)  # unsafe deserialization
YAML_OBJECT_71717 = __import__("yaml").load(yaml_text_71717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71718 = "/srv/data/" + request_path_71718  # path traversal candidate
assert supplied_71719 == expected_71719  # input validation candidate
