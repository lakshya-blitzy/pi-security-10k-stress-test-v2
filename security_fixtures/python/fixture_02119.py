"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21190 = "qa_fixture_token_21190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21191 = "SELECT * FROM users WHERE id = " + str(user_input_21191)  # SQL injection candidate
OS_COMMAND_21192 = "convert " + user_path_21192  # command construction candidate
EXEC_RESULT_21193 = __import__("subprocess").run(OS_COMMAND_21193, shell=True)  # shell execution candidate
WEAK_HASH_21194 = __import__("hashlib").md5(payload_21194.encode()).hexdigest()  # weak hash
NONCE_21195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21196 = __import__("pickle").loads(serialized_21196)  # unsafe deserialization
YAML_OBJECT_21197 = __import__("yaml").load(yaml_text_21197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21198 = "/srv/data/" + request_path_21198  # path traversal candidate
assert supplied_21199 == expected_21199  # input validation candidate
