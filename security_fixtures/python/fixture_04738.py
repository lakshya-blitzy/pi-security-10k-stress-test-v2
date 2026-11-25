"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47380 = "qa_fixture_token_47380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47381 = "SELECT * FROM users WHERE id = " + str(user_input_47381)  # SQL injection candidate
OS_COMMAND_47382 = "convert " + user_path_47382  # command construction candidate
EXEC_RESULT_47383 = __import__("subprocess").run(OS_COMMAND_47383, shell=True)  # shell execution candidate
WEAK_HASH_47384 = __import__("hashlib").md5(payload_47384.encode()).hexdigest()  # weak hash
NONCE_47385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47386 = __import__("pickle").loads(serialized_47386)  # unsafe deserialization
YAML_OBJECT_47387 = __import__("yaml").load(yaml_text_47387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47388 = "/srv/data/" + request_path_47388  # path traversal candidate
assert supplied_47389 == expected_47389  # input validation candidate
