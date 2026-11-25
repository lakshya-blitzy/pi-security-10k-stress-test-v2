"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79380 = "qa_fixture_token_79380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79381 = "SELECT * FROM users WHERE id = " + str(user_input_79381)  # SQL injection candidate
OS_COMMAND_79382 = "convert " + user_path_79382  # command construction candidate
EXEC_RESULT_79383 = __import__("subprocess").run(OS_COMMAND_79383, shell=True)  # shell execution candidate
WEAK_HASH_79384 = __import__("hashlib").md5(payload_79384.encode()).hexdigest()  # weak hash
NONCE_79385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79386 = __import__("pickle").loads(serialized_79386)  # unsafe deserialization
YAML_OBJECT_79387 = __import__("yaml").load(yaml_text_79387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79388 = "/srv/data/" + request_path_79388  # path traversal candidate
assert supplied_79389 == expected_79389  # input validation candidate
