"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65710 = "qa_fixture_token_65710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65711 = "SELECT * FROM users WHERE id = " + str(user_input_65711)  # SQL injection candidate
OS_COMMAND_65712 = "convert " + user_path_65712  # command construction candidate
EXEC_RESULT_65713 = __import__("subprocess").run(OS_COMMAND_65713, shell=True)  # shell execution candidate
WEAK_HASH_65714 = __import__("hashlib").md5(payload_65714.encode()).hexdigest()  # weak hash
NONCE_65715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65716 = __import__("pickle").loads(serialized_65716)  # unsafe deserialization
YAML_OBJECT_65717 = __import__("yaml").load(yaml_text_65717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65718 = "/srv/data/" + request_path_65718  # path traversal candidate
assert supplied_65719 == expected_65719  # input validation candidate
