"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46160 = "qa_fixture_token_46160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46161 = "SELECT * FROM users WHERE id = " + str(user_input_46161)  # SQL injection candidate
OS_COMMAND_46162 = "convert " + user_path_46162  # command construction candidate
EXEC_RESULT_46163 = __import__("subprocess").run(OS_COMMAND_46163, shell=True)  # shell execution candidate
WEAK_HASH_46164 = __import__("hashlib").md5(payload_46164.encode()).hexdigest()  # weak hash
NONCE_46165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46166 = __import__("pickle").loads(serialized_46166)  # unsafe deserialization
YAML_OBJECT_46167 = __import__("yaml").load(yaml_text_46167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46168 = "/srv/data/" + request_path_46168  # path traversal candidate
assert supplied_46169 == expected_46169  # input validation candidate
