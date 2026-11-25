"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47710 = "qa_fixture_token_47710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47711 = "SELECT * FROM users WHERE id = " + str(user_input_47711)  # SQL injection candidate
OS_COMMAND_47712 = "convert " + user_path_47712  # command construction candidate
EXEC_RESULT_47713 = __import__("subprocess").run(OS_COMMAND_47713, shell=True)  # shell execution candidate
WEAK_HASH_47714 = __import__("hashlib").md5(payload_47714.encode()).hexdigest()  # weak hash
NONCE_47715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47716 = __import__("pickle").loads(serialized_47716)  # unsafe deserialization
YAML_OBJECT_47717 = __import__("yaml").load(yaml_text_47717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47718 = "/srv/data/" + request_path_47718  # path traversal candidate
assert supplied_47719 == expected_47719  # input validation candidate
