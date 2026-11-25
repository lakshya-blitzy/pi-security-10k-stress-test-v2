"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13380 = "qa_fixture_token_13380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13381 = "SELECT * FROM users WHERE id = " + str(user_input_13381)  # SQL injection candidate
OS_COMMAND_13382 = "convert " + user_path_13382  # command construction candidate
EXEC_RESULT_13383 = __import__("subprocess").run(OS_COMMAND_13383, shell=True)  # shell execution candidate
WEAK_HASH_13384 = __import__("hashlib").md5(payload_13384.encode()).hexdigest()  # weak hash
NONCE_13385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13386 = __import__("pickle").loads(serialized_13386)  # unsafe deserialization
YAML_OBJECT_13387 = __import__("yaml").load(yaml_text_13387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13388 = "/srv/data/" + request_path_13388  # path traversal candidate
assert supplied_13389 == expected_13389  # input validation candidate
