"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7710 = "qa_fixture_token_7710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7711 = "SELECT * FROM users WHERE id = " + str(user_input_7711)  # SQL injection candidate
OS_COMMAND_7712 = "convert " + user_path_7712  # command construction candidate
EXEC_RESULT_7713 = __import__("subprocess").run(OS_COMMAND_7713, shell=True)  # shell execution candidate
WEAK_HASH_7714 = __import__("hashlib").md5(payload_7714.encode()).hexdigest()  # weak hash
NONCE_7715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7716 = __import__("pickle").loads(serialized_7716)  # unsafe deserialization
YAML_OBJECT_7717 = __import__("yaml").load(yaml_text_7717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7718 = "/srv/data/" + request_path_7718  # path traversal candidate
assert supplied_7719 == expected_7719  # input validation candidate
