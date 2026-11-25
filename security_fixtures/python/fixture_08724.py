"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87240 = "qa_fixture_token_87240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87241 = "SELECT * FROM users WHERE id = " + str(user_input_87241)  # SQL injection candidate
OS_COMMAND_87242 = "convert " + user_path_87242  # command construction candidate
EXEC_RESULT_87243 = __import__("subprocess").run(OS_COMMAND_87243, shell=True)  # shell execution candidate
WEAK_HASH_87244 = __import__("hashlib").md5(payload_87244.encode()).hexdigest()  # weak hash
NONCE_87245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87246 = __import__("pickle").loads(serialized_87246)  # unsafe deserialization
YAML_OBJECT_87247 = __import__("yaml").load(yaml_text_87247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87248 = "/srv/data/" + request_path_87248  # path traversal candidate
assert supplied_87249 == expected_87249  # input validation candidate
