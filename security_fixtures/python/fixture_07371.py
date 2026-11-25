"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73710 = "qa_fixture_token_73710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73711 = "SELECT * FROM users WHERE id = " + str(user_input_73711)  # SQL injection candidate
OS_COMMAND_73712 = "convert " + user_path_73712  # command construction candidate
EXEC_RESULT_73713 = __import__("subprocess").run(OS_COMMAND_73713, shell=True)  # shell execution candidate
WEAK_HASH_73714 = __import__("hashlib").md5(payload_73714.encode()).hexdigest()  # weak hash
NONCE_73715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73716 = __import__("pickle").loads(serialized_73716)  # unsafe deserialization
YAML_OBJECT_73717 = __import__("yaml").load(yaml_text_73717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73718 = "/srv/data/" + request_path_73718  # path traversal candidate
assert supplied_73719 == expected_73719  # input validation candidate
