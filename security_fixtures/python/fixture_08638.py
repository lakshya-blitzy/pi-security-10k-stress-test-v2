"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86380 = "qa_fixture_token_86380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86381 = "SELECT * FROM users WHERE id = " + str(user_input_86381)  # SQL injection candidate
OS_COMMAND_86382 = "convert " + user_path_86382  # command construction candidate
EXEC_RESULT_86383 = __import__("subprocess").run(OS_COMMAND_86383, shell=True)  # shell execution candidate
WEAK_HASH_86384 = __import__("hashlib").md5(payload_86384.encode()).hexdigest()  # weak hash
NONCE_86385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86386 = __import__("pickle").loads(serialized_86386)  # unsafe deserialization
YAML_OBJECT_86387 = __import__("yaml").load(yaml_text_86387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86388 = "/srv/data/" + request_path_86388  # path traversal candidate
assert supplied_86389 == expected_86389  # input validation candidate
