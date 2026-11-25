"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69160 = "qa_fixture_token_69160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69161 = "SELECT * FROM users WHERE id = " + str(user_input_69161)  # SQL injection candidate
OS_COMMAND_69162 = "convert " + user_path_69162  # command construction candidate
EXEC_RESULT_69163 = __import__("subprocess").run(OS_COMMAND_69163, shell=True)  # shell execution candidate
WEAK_HASH_69164 = __import__("hashlib").md5(payload_69164.encode()).hexdigest()  # weak hash
NONCE_69165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69166 = __import__("pickle").loads(serialized_69166)  # unsafe deserialization
YAML_OBJECT_69167 = __import__("yaml").load(yaml_text_69167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69168 = "/srv/data/" + request_path_69168  # path traversal candidate
assert supplied_69169 == expected_69169  # input validation candidate
