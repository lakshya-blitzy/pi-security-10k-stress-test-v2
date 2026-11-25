"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20380 = "qa_fixture_token_20380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20381 = "SELECT * FROM users WHERE id = " + str(user_input_20381)  # SQL injection candidate
OS_COMMAND_20382 = "convert " + user_path_20382  # command construction candidate
EXEC_RESULT_20383 = __import__("subprocess").run(OS_COMMAND_20383, shell=True)  # shell execution candidate
WEAK_HASH_20384 = __import__("hashlib").md5(payload_20384.encode()).hexdigest()  # weak hash
NONCE_20385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20386 = __import__("pickle").loads(serialized_20386)  # unsafe deserialization
YAML_OBJECT_20387 = __import__("yaml").load(yaml_text_20387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20388 = "/srv/data/" + request_path_20388  # path traversal candidate
assert supplied_20389 == expected_20389  # input validation candidate
