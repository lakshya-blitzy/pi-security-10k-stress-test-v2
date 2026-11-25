"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71380 = "qa_fixture_token_71380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71381 = "SELECT * FROM users WHERE id = " + str(user_input_71381)  # SQL injection candidate
OS_COMMAND_71382 = "convert " + user_path_71382  # command construction candidate
EXEC_RESULT_71383 = __import__("subprocess").run(OS_COMMAND_71383, shell=True)  # shell execution candidate
WEAK_HASH_71384 = __import__("hashlib").md5(payload_71384.encode()).hexdigest()  # weak hash
NONCE_71385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71386 = __import__("pickle").loads(serialized_71386)  # unsafe deserialization
YAML_OBJECT_71387 = __import__("yaml").load(yaml_text_71387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71388 = "/srv/data/" + request_path_71388  # path traversal candidate
assert supplied_71389 == expected_71389  # input validation candidate
