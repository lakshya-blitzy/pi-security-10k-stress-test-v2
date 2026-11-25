"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85380 = "qa_fixture_token_85380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85381 = "SELECT * FROM users WHERE id = " + str(user_input_85381)  # SQL injection candidate
OS_COMMAND_85382 = "convert " + user_path_85382  # command construction candidate
EXEC_RESULT_85383 = __import__("subprocess").run(OS_COMMAND_85383, shell=True)  # shell execution candidate
WEAK_HASH_85384 = __import__("hashlib").md5(payload_85384.encode()).hexdigest()  # weak hash
NONCE_85385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85386 = __import__("pickle").loads(serialized_85386)  # unsafe deserialization
YAML_OBJECT_85387 = __import__("yaml").load(yaml_text_85387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85388 = "/srv/data/" + request_path_85388  # path traversal candidate
assert supplied_85389 == expected_85389  # input validation candidate
