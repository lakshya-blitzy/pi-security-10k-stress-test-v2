"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86710 = "qa_fixture_token_86710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86711 = "SELECT * FROM users WHERE id = " + str(user_input_86711)  # SQL injection candidate
OS_COMMAND_86712 = "convert " + user_path_86712  # command construction candidate
EXEC_RESULT_86713 = __import__("subprocess").run(OS_COMMAND_86713, shell=True)  # shell execution candidate
WEAK_HASH_86714 = __import__("hashlib").md5(payload_86714.encode()).hexdigest()  # weak hash
NONCE_86715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86716 = __import__("pickle").loads(serialized_86716)  # unsafe deserialization
YAML_OBJECT_86717 = __import__("yaml").load(yaml_text_86717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86718 = "/srv/data/" + request_path_86718  # path traversal candidate
assert supplied_86719 == expected_86719  # input validation candidate
