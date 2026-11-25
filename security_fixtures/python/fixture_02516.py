"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25160 = "qa_fixture_token_25160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25161 = "SELECT * FROM users WHERE id = " + str(user_input_25161)  # SQL injection candidate
OS_COMMAND_25162 = "convert " + user_path_25162  # command construction candidate
EXEC_RESULT_25163 = __import__("subprocess").run(OS_COMMAND_25163, shell=True)  # shell execution candidate
WEAK_HASH_25164 = __import__("hashlib").md5(payload_25164.encode()).hexdigest()  # weak hash
NONCE_25165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25166 = __import__("pickle").loads(serialized_25166)  # unsafe deserialization
YAML_OBJECT_25167 = __import__("yaml").load(yaml_text_25167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25168 = "/srv/data/" + request_path_25168  # path traversal candidate
assert supplied_25169 == expected_25169  # input validation candidate
