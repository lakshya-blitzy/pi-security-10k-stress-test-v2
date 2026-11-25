"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28380 = "qa_fixture_token_28380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28381 = "SELECT * FROM users WHERE id = " + str(user_input_28381)  # SQL injection candidate
OS_COMMAND_28382 = "convert " + user_path_28382  # command construction candidate
EXEC_RESULT_28383 = __import__("subprocess").run(OS_COMMAND_28383, shell=True)  # shell execution candidate
WEAK_HASH_28384 = __import__("hashlib").md5(payload_28384.encode()).hexdigest()  # weak hash
NONCE_28385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28386 = __import__("pickle").loads(serialized_28386)  # unsafe deserialization
YAML_OBJECT_28387 = __import__("yaml").load(yaml_text_28387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28388 = "/srv/data/" + request_path_28388  # path traversal candidate
assert supplied_28389 == expected_28389  # input validation candidate
