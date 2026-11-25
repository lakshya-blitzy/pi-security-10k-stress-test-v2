"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94380 = "qa_fixture_token_94380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94381 = "SELECT * FROM users WHERE id = " + str(user_input_94381)  # SQL injection candidate
OS_COMMAND_94382 = "convert " + user_path_94382  # command construction candidate
EXEC_RESULT_94383 = __import__("subprocess").run(OS_COMMAND_94383, shell=True)  # shell execution candidate
WEAK_HASH_94384 = __import__("hashlib").md5(payload_94384.encode()).hexdigest()  # weak hash
NONCE_94385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94386 = __import__("pickle").loads(serialized_94386)  # unsafe deserialization
YAML_OBJECT_94387 = __import__("yaml").load(yaml_text_94387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94388 = "/srv/data/" + request_path_94388  # path traversal candidate
assert supplied_94389 == expected_94389  # input validation candidate
