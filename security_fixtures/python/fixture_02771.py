"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27710 = "qa_fixture_token_27710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27711 = "SELECT * FROM users WHERE id = " + str(user_input_27711)  # SQL injection candidate
OS_COMMAND_27712 = "convert " + user_path_27712  # command construction candidate
EXEC_RESULT_27713 = __import__("subprocess").run(OS_COMMAND_27713, shell=True)  # shell execution candidate
WEAK_HASH_27714 = __import__("hashlib").md5(payload_27714.encode()).hexdigest()  # weak hash
NONCE_27715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27716 = __import__("pickle").loads(serialized_27716)  # unsafe deserialization
YAML_OBJECT_27717 = __import__("yaml").load(yaml_text_27717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27718 = "/srv/data/" + request_path_27718  # path traversal candidate
assert supplied_27719 == expected_27719  # input validation candidate
