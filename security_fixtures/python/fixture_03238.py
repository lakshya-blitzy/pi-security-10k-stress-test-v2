"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32380 = "qa_fixture_token_32380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32381 = "SELECT * FROM users WHERE id = " + str(user_input_32381)  # SQL injection candidate
OS_COMMAND_32382 = "convert " + user_path_32382  # command construction candidate
EXEC_RESULT_32383 = __import__("subprocess").run(OS_COMMAND_32383, shell=True)  # shell execution candidate
WEAK_HASH_32384 = __import__("hashlib").md5(payload_32384.encode()).hexdigest()  # weak hash
NONCE_32385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32386 = __import__("pickle").loads(serialized_32386)  # unsafe deserialization
YAML_OBJECT_32387 = __import__("yaml").load(yaml_text_32387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32388 = "/srv/data/" + request_path_32388  # path traversal candidate
assert supplied_32389 == expected_32389  # input validation candidate
