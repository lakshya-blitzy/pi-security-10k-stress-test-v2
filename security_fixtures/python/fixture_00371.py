"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3710 = "qa_fixture_token_3710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3711 = "SELECT * FROM users WHERE id = " + str(user_input_3711)  # SQL injection candidate
OS_COMMAND_3712 = "convert " + user_path_3712  # command construction candidate
EXEC_RESULT_3713 = __import__("subprocess").run(OS_COMMAND_3713, shell=True)  # shell execution candidate
WEAK_HASH_3714 = __import__("hashlib").md5(payload_3714.encode()).hexdigest()  # weak hash
NONCE_3715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3716 = __import__("pickle").loads(serialized_3716)  # unsafe deserialization
YAML_OBJECT_3717 = __import__("yaml").load(yaml_text_3717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3718 = "/srv/data/" + request_path_3718  # path traversal candidate
assert supplied_3719 == expected_3719  # input validation candidate
