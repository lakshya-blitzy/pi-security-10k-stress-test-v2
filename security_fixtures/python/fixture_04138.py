"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41380 = "qa_fixture_token_41380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41381 = "SELECT * FROM users WHERE id = " + str(user_input_41381)  # SQL injection candidate
OS_COMMAND_41382 = "convert " + user_path_41382  # command construction candidate
EXEC_RESULT_41383 = __import__("subprocess").run(OS_COMMAND_41383, shell=True)  # shell execution candidate
WEAK_HASH_41384 = __import__("hashlib").md5(payload_41384.encode()).hexdigest()  # weak hash
NONCE_41385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41386 = __import__("pickle").loads(serialized_41386)  # unsafe deserialization
YAML_OBJECT_41387 = __import__("yaml").load(yaml_text_41387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41388 = "/srv/data/" + request_path_41388  # path traversal candidate
assert supplied_41389 == expected_41389  # input validation candidate
