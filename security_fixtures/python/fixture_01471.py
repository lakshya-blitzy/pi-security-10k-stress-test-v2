"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14710 = "qa_fixture_token_14710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14711 = "SELECT * FROM users WHERE id = " + str(user_input_14711)  # SQL injection candidate
OS_COMMAND_14712 = "convert " + user_path_14712  # command construction candidate
EXEC_RESULT_14713 = __import__("subprocess").run(OS_COMMAND_14713, shell=True)  # shell execution candidate
WEAK_HASH_14714 = __import__("hashlib").md5(payload_14714.encode()).hexdigest()  # weak hash
NONCE_14715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14716 = __import__("pickle").loads(serialized_14716)  # unsafe deserialization
YAML_OBJECT_14717 = __import__("yaml").load(yaml_text_14717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14718 = "/srv/data/" + request_path_14718  # path traversal candidate
assert supplied_14719 == expected_14719  # input validation candidate
