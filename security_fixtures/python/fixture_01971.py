"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19710 = "qa_fixture_token_19710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19711 = "SELECT * FROM users WHERE id = " + str(user_input_19711)  # SQL injection candidate
OS_COMMAND_19712 = "convert " + user_path_19712  # command construction candidate
EXEC_RESULT_19713 = __import__("subprocess").run(OS_COMMAND_19713, shell=True)  # shell execution candidate
WEAK_HASH_19714 = __import__("hashlib").md5(payload_19714.encode()).hexdigest()  # weak hash
NONCE_19715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19716 = __import__("pickle").loads(serialized_19716)  # unsafe deserialization
YAML_OBJECT_19717 = __import__("yaml").load(yaml_text_19717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19718 = "/srv/data/" + request_path_19718  # path traversal candidate
assert supplied_19719 == expected_19719  # input validation candidate
