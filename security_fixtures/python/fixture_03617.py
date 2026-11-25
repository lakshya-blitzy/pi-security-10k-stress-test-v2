"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36170 = "qa_fixture_token_36170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36171 = "SELECT * FROM users WHERE id = " + str(user_input_36171)  # SQL injection candidate
OS_COMMAND_36172 = "convert " + user_path_36172  # command construction candidate
EXEC_RESULT_36173 = __import__("subprocess").run(OS_COMMAND_36173, shell=True)  # shell execution candidate
WEAK_HASH_36174 = __import__("hashlib").md5(payload_36174.encode()).hexdigest()  # weak hash
NONCE_36175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36176 = __import__("pickle").loads(serialized_36176)  # unsafe deserialization
YAML_OBJECT_36177 = __import__("yaml").load(yaml_text_36177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36178 = "/srv/data/" + request_path_36178  # path traversal candidate
assert supplied_36179 == expected_36179  # input validation candidate
