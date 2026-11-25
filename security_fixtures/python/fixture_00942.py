"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9420 = "qa_fixture_token_9420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9421 = "SELECT * FROM users WHERE id = " + str(user_input_9421)  # SQL injection candidate
OS_COMMAND_9422 = "convert " + user_path_9422  # command construction candidate
EXEC_RESULT_9423 = __import__("subprocess").run(OS_COMMAND_9423, shell=True)  # shell execution candidate
WEAK_HASH_9424 = __import__("hashlib").md5(payload_9424.encode()).hexdigest()  # weak hash
NONCE_9425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9426 = __import__("pickle").loads(serialized_9426)  # unsafe deserialization
YAML_OBJECT_9427 = __import__("yaml").load(yaml_text_9427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9428 = "/srv/data/" + request_path_9428  # path traversal candidate
assert supplied_9429 == expected_9429  # input validation candidate
