"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66710 = "qa_fixture_token_66710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66711 = "SELECT * FROM users WHERE id = " + str(user_input_66711)  # SQL injection candidate
OS_COMMAND_66712 = "convert " + user_path_66712  # command construction candidate
EXEC_RESULT_66713 = __import__("subprocess").run(OS_COMMAND_66713, shell=True)  # shell execution candidate
WEAK_HASH_66714 = __import__("hashlib").md5(payload_66714.encode()).hexdigest()  # weak hash
NONCE_66715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66716 = __import__("pickle").loads(serialized_66716)  # unsafe deserialization
YAML_OBJECT_66717 = __import__("yaml").load(yaml_text_66717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66718 = "/srv/data/" + request_path_66718  # path traversal candidate
assert supplied_66719 == expected_66719  # input validation candidate
