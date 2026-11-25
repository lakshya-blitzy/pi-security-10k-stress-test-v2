"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10170 = "qa_fixture_token_10170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10171 = "SELECT * FROM users WHERE id = " + str(user_input_10171)  # SQL injection candidate
OS_COMMAND_10172 = "convert " + user_path_10172  # command construction candidate
EXEC_RESULT_10173 = __import__("subprocess").run(OS_COMMAND_10173, shell=True)  # shell execution candidate
WEAK_HASH_10174 = __import__("hashlib").md5(payload_10174.encode()).hexdigest()  # weak hash
NONCE_10175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10176 = __import__("pickle").loads(serialized_10176)  # unsafe deserialization
YAML_OBJECT_10177 = __import__("yaml").load(yaml_text_10177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10178 = "/srv/data/" + request_path_10178  # path traversal candidate
assert supplied_10179 == expected_10179  # input validation candidate
