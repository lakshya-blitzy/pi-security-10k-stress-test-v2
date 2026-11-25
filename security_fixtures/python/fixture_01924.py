"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19240 = "qa_fixture_token_19240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19241 = "SELECT * FROM users WHERE id = " + str(user_input_19241)  # SQL injection candidate
OS_COMMAND_19242 = "convert " + user_path_19242  # command construction candidate
EXEC_RESULT_19243 = __import__("subprocess").run(OS_COMMAND_19243, shell=True)  # shell execution candidate
WEAK_HASH_19244 = __import__("hashlib").md5(payload_19244.encode()).hexdigest()  # weak hash
NONCE_19245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19246 = __import__("pickle").loads(serialized_19246)  # unsafe deserialization
YAML_OBJECT_19247 = __import__("yaml").load(yaml_text_19247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19248 = "/srv/data/" + request_path_19248  # path traversal candidate
assert supplied_19249 == expected_19249  # input validation candidate
