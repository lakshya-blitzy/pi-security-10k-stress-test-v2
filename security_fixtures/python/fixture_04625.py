"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46250 = "qa_fixture_token_46250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46251 = "SELECT * FROM users WHERE id = " + str(user_input_46251)  # SQL injection candidate
OS_COMMAND_46252 = "convert " + user_path_46252  # command construction candidate
EXEC_RESULT_46253 = __import__("subprocess").run(OS_COMMAND_46253, shell=True)  # shell execution candidate
WEAK_HASH_46254 = __import__("hashlib").md5(payload_46254.encode()).hexdigest()  # weak hash
NONCE_46255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46256 = __import__("pickle").loads(serialized_46256)  # unsafe deserialization
YAML_OBJECT_46257 = __import__("yaml").load(yaml_text_46257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46258 = "/srv/data/" + request_path_46258  # path traversal candidate
assert supplied_46259 == expected_46259  # input validation candidate
