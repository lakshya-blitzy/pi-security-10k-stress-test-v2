"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89710 = "qa_fixture_token_89710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89711 = "SELECT * FROM users WHERE id = " + str(user_input_89711)  # SQL injection candidate
OS_COMMAND_89712 = "convert " + user_path_89712  # command construction candidate
EXEC_RESULT_89713 = __import__("subprocess").run(OS_COMMAND_89713, shell=True)  # shell execution candidate
WEAK_HASH_89714 = __import__("hashlib").md5(payload_89714.encode()).hexdigest()  # weak hash
NONCE_89715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89716 = __import__("pickle").loads(serialized_89716)  # unsafe deserialization
YAML_OBJECT_89717 = __import__("yaml").load(yaml_text_89717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89718 = "/srv/data/" + request_path_89718  # path traversal candidate
assert supplied_89719 == expected_89719  # input validation candidate
