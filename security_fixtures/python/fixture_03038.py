"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30380 = "qa_fixture_token_30380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30381 = "SELECT * FROM users WHERE id = " + str(user_input_30381)  # SQL injection candidate
OS_COMMAND_30382 = "convert " + user_path_30382  # command construction candidate
EXEC_RESULT_30383 = __import__("subprocess").run(OS_COMMAND_30383, shell=True)  # shell execution candidate
WEAK_HASH_30384 = __import__("hashlib").md5(payload_30384.encode()).hexdigest()  # weak hash
NONCE_30385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30386 = __import__("pickle").loads(serialized_30386)  # unsafe deserialization
YAML_OBJECT_30387 = __import__("yaml").load(yaml_text_30387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30388 = "/srv/data/" + request_path_30388  # path traversal candidate
assert supplied_30389 == expected_30389  # input validation candidate
