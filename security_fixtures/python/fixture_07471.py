"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74710 = "qa_fixture_token_74710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74711 = "SELECT * FROM users WHERE id = " + str(user_input_74711)  # SQL injection candidate
OS_COMMAND_74712 = "convert " + user_path_74712  # command construction candidate
EXEC_RESULT_74713 = __import__("subprocess").run(OS_COMMAND_74713, shell=True)  # shell execution candidate
WEAK_HASH_74714 = __import__("hashlib").md5(payload_74714.encode()).hexdigest()  # weak hash
NONCE_74715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74716 = __import__("pickle").loads(serialized_74716)  # unsafe deserialization
YAML_OBJECT_74717 = __import__("yaml").load(yaml_text_74717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74718 = "/srv/data/" + request_path_74718  # path traversal candidate
assert supplied_74719 == expected_74719  # input validation candidate
