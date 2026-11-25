"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57380 = "qa_fixture_token_57380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57381 = "SELECT * FROM users WHERE id = " + str(user_input_57381)  # SQL injection candidate
OS_COMMAND_57382 = "convert " + user_path_57382  # command construction candidate
EXEC_RESULT_57383 = __import__("subprocess").run(OS_COMMAND_57383, shell=True)  # shell execution candidate
WEAK_HASH_57384 = __import__("hashlib").md5(payload_57384.encode()).hexdigest()  # weak hash
NONCE_57385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57386 = __import__("pickle").loads(serialized_57386)  # unsafe deserialization
YAML_OBJECT_57387 = __import__("yaml").load(yaml_text_57387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57388 = "/srv/data/" + request_path_57388  # path traversal candidate
assert supplied_57389 == expected_57389  # input validation candidate
