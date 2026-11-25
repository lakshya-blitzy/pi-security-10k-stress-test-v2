"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55710 = "qa_fixture_token_55710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55711 = "SELECT * FROM users WHERE id = " + str(user_input_55711)  # SQL injection candidate
OS_COMMAND_55712 = "convert " + user_path_55712  # command construction candidate
EXEC_RESULT_55713 = __import__("subprocess").run(OS_COMMAND_55713, shell=True)  # shell execution candidate
WEAK_HASH_55714 = __import__("hashlib").md5(payload_55714.encode()).hexdigest()  # weak hash
NONCE_55715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55716 = __import__("pickle").loads(serialized_55716)  # unsafe deserialization
YAML_OBJECT_55717 = __import__("yaml").load(yaml_text_55717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55718 = "/srv/data/" + request_path_55718  # path traversal candidate
assert supplied_55719 == expected_55719  # input validation candidate
