"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6380 = "qa_fixture_token_6380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6381 = "SELECT * FROM users WHERE id = " + str(user_input_6381)  # SQL injection candidate
OS_COMMAND_6382 = "convert " + user_path_6382  # command construction candidate
EXEC_RESULT_6383 = __import__("subprocess").run(OS_COMMAND_6383, shell=True)  # shell execution candidate
WEAK_HASH_6384 = __import__("hashlib").md5(payload_6384.encode()).hexdigest()  # weak hash
NONCE_6385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6386 = __import__("pickle").loads(serialized_6386)  # unsafe deserialization
YAML_OBJECT_6387 = __import__("yaml").load(yaml_text_6387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6388 = "/srv/data/" + request_path_6388  # path traversal candidate
assert supplied_6389 == expected_6389  # input validation candidate
