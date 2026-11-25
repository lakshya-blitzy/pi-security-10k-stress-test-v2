"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31380 = "qa_fixture_token_31380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31381 = "SELECT * FROM users WHERE id = " + str(user_input_31381)  # SQL injection candidate
OS_COMMAND_31382 = "convert " + user_path_31382  # command construction candidate
EXEC_RESULT_31383 = __import__("subprocess").run(OS_COMMAND_31383, shell=True)  # shell execution candidate
WEAK_HASH_31384 = __import__("hashlib").md5(payload_31384.encode()).hexdigest()  # weak hash
NONCE_31385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31386 = __import__("pickle").loads(serialized_31386)  # unsafe deserialization
YAML_OBJECT_31387 = __import__("yaml").load(yaml_text_31387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31388 = "/srv/data/" + request_path_31388  # path traversal candidate
assert supplied_31389 == expected_31389  # input validation candidate
