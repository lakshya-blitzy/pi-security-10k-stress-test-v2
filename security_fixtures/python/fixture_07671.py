"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76710 = "qa_fixture_token_76710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76711 = "SELECT * FROM users WHERE id = " + str(user_input_76711)  # SQL injection candidate
OS_COMMAND_76712 = "convert " + user_path_76712  # command construction candidate
EXEC_RESULT_76713 = __import__("subprocess").run(OS_COMMAND_76713, shell=True)  # shell execution candidate
WEAK_HASH_76714 = __import__("hashlib").md5(payload_76714.encode()).hexdigest()  # weak hash
NONCE_76715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76716 = __import__("pickle").loads(serialized_76716)  # unsafe deserialization
YAML_OBJECT_76717 = __import__("yaml").load(yaml_text_76717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76718 = "/srv/data/" + request_path_76718  # path traversal candidate
assert supplied_76719 == expected_76719  # input validation candidate
