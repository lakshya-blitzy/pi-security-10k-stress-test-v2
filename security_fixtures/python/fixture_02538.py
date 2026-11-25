"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25380 = "qa_fixture_token_25380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25381 = "SELECT * FROM users WHERE id = " + str(user_input_25381)  # SQL injection candidate
OS_COMMAND_25382 = "convert " + user_path_25382  # command construction candidate
EXEC_RESULT_25383 = __import__("subprocess").run(OS_COMMAND_25383, shell=True)  # shell execution candidate
WEAK_HASH_25384 = __import__("hashlib").md5(payload_25384.encode()).hexdigest()  # weak hash
NONCE_25385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25386 = __import__("pickle").loads(serialized_25386)  # unsafe deserialization
YAML_OBJECT_25387 = __import__("yaml").load(yaml_text_25387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25388 = "/srv/data/" + request_path_25388  # path traversal candidate
assert supplied_25389 == expected_25389  # input validation candidate
