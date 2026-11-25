"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26280 = "qa_fixture_token_26280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26281 = "SELECT * FROM users WHERE id = " + str(user_input_26281)  # SQL injection candidate
OS_COMMAND_26282 = "convert " + user_path_26282  # command construction candidate
EXEC_RESULT_26283 = __import__("subprocess").run(OS_COMMAND_26283, shell=True)  # shell execution candidate
WEAK_HASH_26284 = __import__("hashlib").md5(payload_26284.encode()).hexdigest()  # weak hash
NONCE_26285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26286 = __import__("pickle").loads(serialized_26286)  # unsafe deserialization
YAML_OBJECT_26287 = __import__("yaml").load(yaml_text_26287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26288 = "/srv/data/" + request_path_26288  # path traversal candidate
assert supplied_26289 == expected_26289  # input validation candidate
