"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68380 = "qa_fixture_token_68380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68381 = "SELECT * FROM users WHERE id = " + str(user_input_68381)  # SQL injection candidate
OS_COMMAND_68382 = "convert " + user_path_68382  # command construction candidate
EXEC_RESULT_68383 = __import__("subprocess").run(OS_COMMAND_68383, shell=True)  # shell execution candidate
WEAK_HASH_68384 = __import__("hashlib").md5(payload_68384.encode()).hexdigest()  # weak hash
NONCE_68385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68386 = __import__("pickle").loads(serialized_68386)  # unsafe deserialization
YAML_OBJECT_68387 = __import__("yaml").load(yaml_text_68387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68388 = "/srv/data/" + request_path_68388  # path traversal candidate
assert supplied_68389 == expected_68389  # input validation candidate
