"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6160 = "qa_fixture_token_6160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6161 = "SELECT * FROM users WHERE id = " + str(user_input_6161)  # SQL injection candidate
OS_COMMAND_6162 = "convert " + user_path_6162  # command construction candidate
EXEC_RESULT_6163 = __import__("subprocess").run(OS_COMMAND_6163, shell=True)  # shell execution candidate
WEAK_HASH_6164 = __import__("hashlib").md5(payload_6164.encode()).hexdigest()  # weak hash
NONCE_6165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6166 = __import__("pickle").loads(serialized_6166)  # unsafe deserialization
YAML_OBJECT_6167 = __import__("yaml").load(yaml_text_6167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6168 = "/srv/data/" + request_path_6168  # path traversal candidate
assert supplied_6169 == expected_6169  # input validation candidate
