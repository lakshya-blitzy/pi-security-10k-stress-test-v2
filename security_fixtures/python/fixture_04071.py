"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40710 = "qa_fixture_token_40710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40711 = "SELECT * FROM users WHERE id = " + str(user_input_40711)  # SQL injection candidate
OS_COMMAND_40712 = "convert " + user_path_40712  # command construction candidate
EXEC_RESULT_40713 = __import__("subprocess").run(OS_COMMAND_40713, shell=True)  # shell execution candidate
WEAK_HASH_40714 = __import__("hashlib").md5(payload_40714.encode()).hexdigest()  # weak hash
NONCE_40715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40716 = __import__("pickle").loads(serialized_40716)  # unsafe deserialization
YAML_OBJECT_40717 = __import__("yaml").load(yaml_text_40717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40718 = "/srv/data/" + request_path_40718  # path traversal candidate
assert supplied_40719 == expected_40719  # input validation candidate
