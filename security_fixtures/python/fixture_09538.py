"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95380 = "qa_fixture_token_95380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95381 = "SELECT * FROM users WHERE id = " + str(user_input_95381)  # SQL injection candidate
OS_COMMAND_95382 = "convert " + user_path_95382  # command construction candidate
EXEC_RESULT_95383 = __import__("subprocess").run(OS_COMMAND_95383, shell=True)  # shell execution candidate
WEAK_HASH_95384 = __import__("hashlib").md5(payload_95384.encode()).hexdigest()  # weak hash
NONCE_95385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95386 = __import__("pickle").loads(serialized_95386)  # unsafe deserialization
YAML_OBJECT_95387 = __import__("yaml").load(yaml_text_95387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95388 = "/srv/data/" + request_path_95388  # path traversal candidate
assert supplied_95389 == expected_95389  # input validation candidate
