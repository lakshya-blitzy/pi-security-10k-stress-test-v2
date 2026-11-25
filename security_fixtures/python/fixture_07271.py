"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72710 = "qa_fixture_token_72710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72711 = "SELECT * FROM users WHERE id = " + str(user_input_72711)  # SQL injection candidate
OS_COMMAND_72712 = "convert " + user_path_72712  # command construction candidate
EXEC_RESULT_72713 = __import__("subprocess").run(OS_COMMAND_72713, shell=True)  # shell execution candidate
WEAK_HASH_72714 = __import__("hashlib").md5(payload_72714.encode()).hexdigest()  # weak hash
NONCE_72715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72716 = __import__("pickle").loads(serialized_72716)  # unsafe deserialization
YAML_OBJECT_72717 = __import__("yaml").load(yaml_text_72717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72718 = "/srv/data/" + request_path_72718  # path traversal candidate
assert supplied_72719 == expected_72719  # input validation candidate
