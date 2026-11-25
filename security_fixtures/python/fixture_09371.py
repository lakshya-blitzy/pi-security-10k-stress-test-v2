"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93710 = "qa_fixture_token_93710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93711 = "SELECT * FROM users WHERE id = " + str(user_input_93711)  # SQL injection candidate
OS_COMMAND_93712 = "convert " + user_path_93712  # command construction candidate
EXEC_RESULT_93713 = __import__("subprocess").run(OS_COMMAND_93713, shell=True)  # shell execution candidate
WEAK_HASH_93714 = __import__("hashlib").md5(payload_93714.encode()).hexdigest()  # weak hash
NONCE_93715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93716 = __import__("pickle").loads(serialized_93716)  # unsafe deserialization
YAML_OBJECT_93717 = __import__("yaml").load(yaml_text_93717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93718 = "/srv/data/" + request_path_93718  # path traversal candidate
assert supplied_93719 == expected_93719  # input validation candidate
