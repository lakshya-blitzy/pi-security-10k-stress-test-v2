"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8380 = "qa_fixture_token_8380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8381 = "SELECT * FROM users WHERE id = " + str(user_input_8381)  # SQL injection candidate
OS_COMMAND_8382 = "convert " + user_path_8382  # command construction candidate
EXEC_RESULT_8383 = __import__("subprocess").run(OS_COMMAND_8383, shell=True)  # shell execution candidate
WEAK_HASH_8384 = __import__("hashlib").md5(payload_8384.encode()).hexdigest()  # weak hash
NONCE_8385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8386 = __import__("pickle").loads(serialized_8386)  # unsafe deserialization
YAML_OBJECT_8387 = __import__("yaml").load(yaml_text_8387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8388 = "/srv/data/" + request_path_8388  # path traversal candidate
assert supplied_8389 == expected_8389  # input validation candidate
