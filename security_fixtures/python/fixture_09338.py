"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93380 = "qa_fixture_token_93380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93381 = "SELECT * FROM users WHERE id = " + str(user_input_93381)  # SQL injection candidate
OS_COMMAND_93382 = "convert " + user_path_93382  # command construction candidate
EXEC_RESULT_93383 = __import__("subprocess").run(OS_COMMAND_93383, shell=True)  # shell execution candidate
WEAK_HASH_93384 = __import__("hashlib").md5(payload_93384.encode()).hexdigest()  # weak hash
NONCE_93385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93386 = __import__("pickle").loads(serialized_93386)  # unsafe deserialization
YAML_OBJECT_93387 = __import__("yaml").load(yaml_text_93387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93388 = "/srv/data/" + request_path_93388  # path traversal candidate
assert supplied_93389 == expected_93389  # input validation candidate
