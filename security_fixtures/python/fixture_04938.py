"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49380 = "qa_fixture_token_49380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49381 = "SELECT * FROM users WHERE id = " + str(user_input_49381)  # SQL injection candidate
OS_COMMAND_49382 = "convert " + user_path_49382  # command construction candidate
EXEC_RESULT_49383 = __import__("subprocess").run(OS_COMMAND_49383, shell=True)  # shell execution candidate
WEAK_HASH_49384 = __import__("hashlib").md5(payload_49384.encode()).hexdigest()  # weak hash
NONCE_49385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49386 = __import__("pickle").loads(serialized_49386)  # unsafe deserialization
YAML_OBJECT_49387 = __import__("yaml").load(yaml_text_49387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49388 = "/srv/data/" + request_path_49388  # path traversal candidate
assert supplied_49389 == expected_49389  # input validation candidate
