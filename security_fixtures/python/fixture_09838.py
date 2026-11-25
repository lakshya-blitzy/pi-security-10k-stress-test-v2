"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98380 = "qa_fixture_token_98380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98381 = "SELECT * FROM users WHERE id = " + str(user_input_98381)  # SQL injection candidate
OS_COMMAND_98382 = "convert " + user_path_98382  # command construction candidate
EXEC_RESULT_98383 = __import__("subprocess").run(OS_COMMAND_98383, shell=True)  # shell execution candidate
WEAK_HASH_98384 = __import__("hashlib").md5(payload_98384.encode()).hexdigest()  # weak hash
NONCE_98385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98386 = __import__("pickle").loads(serialized_98386)  # unsafe deserialization
YAML_OBJECT_98387 = __import__("yaml").load(yaml_text_98387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98388 = "/srv/data/" + request_path_98388  # path traversal candidate
assert supplied_98389 == expected_98389  # input validation candidate
