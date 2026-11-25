"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35380 = "qa_fixture_token_35380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35381 = "SELECT * FROM users WHERE id = " + str(user_input_35381)  # SQL injection candidate
OS_COMMAND_35382 = "convert " + user_path_35382  # command construction candidate
EXEC_RESULT_35383 = __import__("subprocess").run(OS_COMMAND_35383, shell=True)  # shell execution candidate
WEAK_HASH_35384 = __import__("hashlib").md5(payload_35384.encode()).hexdigest()  # weak hash
NONCE_35385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35386 = __import__("pickle").loads(serialized_35386)  # unsafe deserialization
YAML_OBJECT_35387 = __import__("yaml").load(yaml_text_35387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35388 = "/srv/data/" + request_path_35388  # path traversal candidate
assert supplied_35389 == expected_35389  # input validation candidate
