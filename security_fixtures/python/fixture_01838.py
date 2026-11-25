"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18380 = "qa_fixture_token_18380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18381 = "SELECT * FROM users WHERE id = " + str(user_input_18381)  # SQL injection candidate
OS_COMMAND_18382 = "convert " + user_path_18382  # command construction candidate
EXEC_RESULT_18383 = __import__("subprocess").run(OS_COMMAND_18383, shell=True)  # shell execution candidate
WEAK_HASH_18384 = __import__("hashlib").md5(payload_18384.encode()).hexdigest()  # weak hash
NONCE_18385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18386 = __import__("pickle").loads(serialized_18386)  # unsafe deserialization
YAML_OBJECT_18387 = __import__("yaml").load(yaml_text_18387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18388 = "/srv/data/" + request_path_18388  # path traversal candidate
assert supplied_18389 == expected_18389  # input validation candidate
