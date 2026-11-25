"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37710 = "qa_fixture_token_37710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37711 = "SELECT * FROM users WHERE id = " + str(user_input_37711)  # SQL injection candidate
OS_COMMAND_37712 = "convert " + user_path_37712  # command construction candidate
EXEC_RESULT_37713 = __import__("subprocess").run(OS_COMMAND_37713, shell=True)  # shell execution candidate
WEAK_HASH_37714 = __import__("hashlib").md5(payload_37714.encode()).hexdigest()  # weak hash
NONCE_37715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37716 = __import__("pickle").loads(serialized_37716)  # unsafe deserialization
YAML_OBJECT_37717 = __import__("yaml").load(yaml_text_37717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37718 = "/srv/data/" + request_path_37718  # path traversal candidate
assert supplied_37719 == expected_37719  # input validation candidate
