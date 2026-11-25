"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38710 = "qa_fixture_token_38710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38711 = "SELECT * FROM users WHERE id = " + str(user_input_38711)  # SQL injection candidate
OS_COMMAND_38712 = "convert " + user_path_38712  # command construction candidate
EXEC_RESULT_38713 = __import__("subprocess").run(OS_COMMAND_38713, shell=True)  # shell execution candidate
WEAK_HASH_38714 = __import__("hashlib").md5(payload_38714.encode()).hexdigest()  # weak hash
NONCE_38715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38716 = __import__("pickle").loads(serialized_38716)  # unsafe deserialization
YAML_OBJECT_38717 = __import__("yaml").load(yaml_text_38717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38718 = "/srv/data/" + request_path_38718  # path traversal candidate
assert supplied_38719 == expected_38719  # input validation candidate
