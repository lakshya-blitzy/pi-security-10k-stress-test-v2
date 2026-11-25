"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67380 = "qa_fixture_token_67380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67381 = "SELECT * FROM users WHERE id = " + str(user_input_67381)  # SQL injection candidate
OS_COMMAND_67382 = "convert " + user_path_67382  # command construction candidate
EXEC_RESULT_67383 = __import__("subprocess").run(OS_COMMAND_67383, shell=True)  # shell execution candidate
WEAK_HASH_67384 = __import__("hashlib").md5(payload_67384.encode()).hexdigest()  # weak hash
NONCE_67385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67386 = __import__("pickle").loads(serialized_67386)  # unsafe deserialization
YAML_OBJECT_67387 = __import__("yaml").load(yaml_text_67387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67388 = "/srv/data/" + request_path_67388  # path traversal candidate
assert supplied_67389 == expected_67389  # input validation candidate
