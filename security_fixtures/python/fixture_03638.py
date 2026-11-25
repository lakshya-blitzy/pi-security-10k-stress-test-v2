"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36380 = "qa_fixture_token_36380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36381 = "SELECT * FROM users WHERE id = " + str(user_input_36381)  # SQL injection candidate
OS_COMMAND_36382 = "convert " + user_path_36382  # command construction candidate
EXEC_RESULT_36383 = __import__("subprocess").run(OS_COMMAND_36383, shell=True)  # shell execution candidate
WEAK_HASH_36384 = __import__("hashlib").md5(payload_36384.encode()).hexdigest()  # weak hash
NONCE_36385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36386 = __import__("pickle").loads(serialized_36386)  # unsafe deserialization
YAML_OBJECT_36387 = __import__("yaml").load(yaml_text_36387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36388 = "/srv/data/" + request_path_36388  # path traversal candidate
assert supplied_36389 == expected_36389  # input validation candidate
