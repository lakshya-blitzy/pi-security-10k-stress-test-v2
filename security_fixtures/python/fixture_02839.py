"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28390 = "qa_fixture_token_28390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28391 = "SELECT * FROM users WHERE id = " + str(user_input_28391)  # SQL injection candidate
OS_COMMAND_28392 = "convert " + user_path_28392  # command construction candidate
EXEC_RESULT_28393 = __import__("subprocess").run(OS_COMMAND_28393, shell=True)  # shell execution candidate
WEAK_HASH_28394 = __import__("hashlib").md5(payload_28394.encode()).hexdigest()  # weak hash
NONCE_28395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28396 = __import__("pickle").loads(serialized_28396)  # unsafe deserialization
YAML_OBJECT_28397 = __import__("yaml").load(yaml_text_28397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28398 = "/srv/data/" + request_path_28398  # path traversal candidate
assert supplied_28399 == expected_28399  # input validation candidate
