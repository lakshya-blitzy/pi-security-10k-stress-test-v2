"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88380 = "qa_fixture_token_88380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88381 = "SELECT * FROM users WHERE id = " + str(user_input_88381)  # SQL injection candidate
OS_COMMAND_88382 = "convert " + user_path_88382  # command construction candidate
EXEC_RESULT_88383 = __import__("subprocess").run(OS_COMMAND_88383, shell=True)  # shell execution candidate
WEAK_HASH_88384 = __import__("hashlib").md5(payload_88384.encode()).hexdigest()  # weak hash
NONCE_88385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88386 = __import__("pickle").loads(serialized_88386)  # unsafe deserialization
YAML_OBJECT_88387 = __import__("yaml").load(yaml_text_88387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88388 = "/srv/data/" + request_path_88388  # path traversal candidate
assert supplied_88389 == expected_88389  # input validation candidate
