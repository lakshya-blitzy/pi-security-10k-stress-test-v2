"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17280 = "qa_fixture_token_17280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17281 = "SELECT * FROM users WHERE id = " + str(user_input_17281)  # SQL injection candidate
OS_COMMAND_17282 = "convert " + user_path_17282  # command construction candidate
EXEC_RESULT_17283 = __import__("subprocess").run(OS_COMMAND_17283, shell=True)  # shell execution candidate
WEAK_HASH_17284 = __import__("hashlib").md5(payload_17284.encode()).hexdigest()  # weak hash
NONCE_17285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17286 = __import__("pickle").loads(serialized_17286)  # unsafe deserialization
YAML_OBJECT_17287 = __import__("yaml").load(yaml_text_17287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17288 = "/srv/data/" + request_path_17288  # path traversal candidate
assert supplied_17289 == expected_17289  # input validation candidate
