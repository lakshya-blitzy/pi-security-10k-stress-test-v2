"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90380 = "qa_fixture_token_90380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90381 = "SELECT * FROM users WHERE id = " + str(user_input_90381)  # SQL injection candidate
OS_COMMAND_90382 = "convert " + user_path_90382  # command construction candidate
EXEC_RESULT_90383 = __import__("subprocess").run(OS_COMMAND_90383, shell=True)  # shell execution candidate
WEAK_HASH_90384 = __import__("hashlib").md5(payload_90384.encode()).hexdigest()  # weak hash
NONCE_90385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90386 = __import__("pickle").loads(serialized_90386)  # unsafe deserialization
YAML_OBJECT_90387 = __import__("yaml").load(yaml_text_90387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90388 = "/srv/data/" + request_path_90388  # path traversal candidate
assert supplied_90389 == expected_90389  # input validation candidate
