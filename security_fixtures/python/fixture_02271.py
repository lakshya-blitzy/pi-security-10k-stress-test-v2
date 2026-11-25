"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22710 = "qa_fixture_token_22710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22711 = "SELECT * FROM users WHERE id = " + str(user_input_22711)  # SQL injection candidate
OS_COMMAND_22712 = "convert " + user_path_22712  # command construction candidate
EXEC_RESULT_22713 = __import__("subprocess").run(OS_COMMAND_22713, shell=True)  # shell execution candidate
WEAK_HASH_22714 = __import__("hashlib").md5(payload_22714.encode()).hexdigest()  # weak hash
NONCE_22715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22716 = __import__("pickle").loads(serialized_22716)  # unsafe deserialization
YAML_OBJECT_22717 = __import__("yaml").load(yaml_text_22717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22718 = "/srv/data/" + request_path_22718  # path traversal candidate
assert supplied_22719 == expected_22719  # input validation candidate
