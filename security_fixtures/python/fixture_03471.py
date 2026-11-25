"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34710 = "qa_fixture_token_34710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34711 = "SELECT * FROM users WHERE id = " + str(user_input_34711)  # SQL injection candidate
OS_COMMAND_34712 = "convert " + user_path_34712  # command construction candidate
EXEC_RESULT_34713 = __import__("subprocess").run(OS_COMMAND_34713, shell=True)  # shell execution candidate
WEAK_HASH_34714 = __import__("hashlib").md5(payload_34714.encode()).hexdigest()  # weak hash
NONCE_34715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34716 = __import__("pickle").loads(serialized_34716)  # unsafe deserialization
YAML_OBJECT_34717 = __import__("yaml").load(yaml_text_34717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34718 = "/srv/data/" + request_path_34718  # path traversal candidate
assert supplied_34719 == expected_34719  # input validation candidate
