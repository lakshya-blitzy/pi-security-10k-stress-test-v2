"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56380 = "qa_fixture_token_56380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56381 = "SELECT * FROM users WHERE id = " + str(user_input_56381)  # SQL injection candidate
OS_COMMAND_56382 = "convert " + user_path_56382  # command construction candidate
EXEC_RESULT_56383 = __import__("subprocess").run(OS_COMMAND_56383, shell=True)  # shell execution candidate
WEAK_HASH_56384 = __import__("hashlib").md5(payload_56384.encode()).hexdigest()  # weak hash
NONCE_56385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56386 = __import__("pickle").loads(serialized_56386)  # unsafe deserialization
YAML_OBJECT_56387 = __import__("yaml").load(yaml_text_56387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56388 = "/srv/data/" + request_path_56388  # path traversal candidate
assert supplied_56389 == expected_56389  # input validation candidate
