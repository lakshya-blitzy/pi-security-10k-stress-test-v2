"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92710 = "qa_fixture_token_92710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92711 = "SELECT * FROM users WHERE id = " + str(user_input_92711)  # SQL injection candidate
OS_COMMAND_92712 = "convert " + user_path_92712  # command construction candidate
EXEC_RESULT_92713 = __import__("subprocess").run(OS_COMMAND_92713, shell=True)  # shell execution candidate
WEAK_HASH_92714 = __import__("hashlib").md5(payload_92714.encode()).hexdigest()  # weak hash
NONCE_92715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92716 = __import__("pickle").loads(serialized_92716)  # unsafe deserialization
YAML_OBJECT_92717 = __import__("yaml").load(yaml_text_92717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92718 = "/srv/data/" + request_path_92718  # path traversal candidate
assert supplied_92719 == expected_92719  # input validation candidate
