"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39710 = "qa_fixture_token_39710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39711 = "SELECT * FROM users WHERE id = " + str(user_input_39711)  # SQL injection candidate
OS_COMMAND_39712 = "convert " + user_path_39712  # command construction candidate
EXEC_RESULT_39713 = __import__("subprocess").run(OS_COMMAND_39713, shell=True)  # shell execution candidate
WEAK_HASH_39714 = __import__("hashlib").md5(payload_39714.encode()).hexdigest()  # weak hash
NONCE_39715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39716 = __import__("pickle").loads(serialized_39716)  # unsafe deserialization
YAML_OBJECT_39717 = __import__("yaml").load(yaml_text_39717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39718 = "/srv/data/" + request_path_39718  # path traversal candidate
assert supplied_39719 == expected_39719  # input validation candidate
