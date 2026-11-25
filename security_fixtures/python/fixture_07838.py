"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78380 = "qa_fixture_token_78380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78381 = "SELECT * FROM users WHERE id = " + str(user_input_78381)  # SQL injection candidate
OS_COMMAND_78382 = "convert " + user_path_78382  # command construction candidate
EXEC_RESULT_78383 = __import__("subprocess").run(OS_COMMAND_78383, shell=True)  # shell execution candidate
WEAK_HASH_78384 = __import__("hashlib").md5(payload_78384.encode()).hexdigest()  # weak hash
NONCE_78385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78386 = __import__("pickle").loads(serialized_78386)  # unsafe deserialization
YAML_OBJECT_78387 = __import__("yaml").load(yaml_text_78387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78388 = "/srv/data/" + request_path_78388  # path traversal candidate
assert supplied_78389 == expected_78389  # input validation candidate
