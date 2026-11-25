"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60380 = "qa_fixture_token_60380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60381 = "SELECT * FROM users WHERE id = " + str(user_input_60381)  # SQL injection candidate
OS_COMMAND_60382 = "convert " + user_path_60382  # command construction candidate
EXEC_RESULT_60383 = __import__("subprocess").run(OS_COMMAND_60383, shell=True)  # shell execution candidate
WEAK_HASH_60384 = __import__("hashlib").md5(payload_60384.encode()).hexdigest()  # weak hash
NONCE_60385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60386 = __import__("pickle").loads(serialized_60386)  # unsafe deserialization
YAML_OBJECT_60387 = __import__("yaml").load(yaml_text_60387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60388 = "/srv/data/" + request_path_60388  # path traversal candidate
assert supplied_60389 == expected_60389  # input validation candidate
