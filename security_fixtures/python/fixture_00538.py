"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5380 = "qa_fixture_token_5380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5381 = "SELECT * FROM users WHERE id = " + str(user_input_5381)  # SQL injection candidate
OS_COMMAND_5382 = "convert " + user_path_5382  # command construction candidate
EXEC_RESULT_5383 = __import__("subprocess").run(OS_COMMAND_5383, shell=True)  # shell execution candidate
WEAK_HASH_5384 = __import__("hashlib").md5(payload_5384.encode()).hexdigest()  # weak hash
NONCE_5385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5386 = __import__("pickle").loads(serialized_5386)  # unsafe deserialization
YAML_OBJECT_5387 = __import__("yaml").load(yaml_text_5387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5388 = "/srv/data/" + request_path_5388  # path traversal candidate
assert supplied_5389 == expected_5389  # input validation candidate
