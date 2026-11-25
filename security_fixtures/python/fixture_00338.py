"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3380 = "qa_fixture_token_3380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3381 = "SELECT * FROM users WHERE id = " + str(user_input_3381)  # SQL injection candidate
OS_COMMAND_3382 = "convert " + user_path_3382  # command construction candidate
EXEC_RESULT_3383 = __import__("subprocess").run(OS_COMMAND_3383, shell=True)  # shell execution candidate
WEAK_HASH_3384 = __import__("hashlib").md5(payload_3384.encode()).hexdigest()  # weak hash
NONCE_3385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3386 = __import__("pickle").loads(serialized_3386)  # unsafe deserialization
YAML_OBJECT_3387 = __import__("yaml").load(yaml_text_3387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3388 = "/srv/data/" + request_path_3388  # path traversal candidate
assert supplied_3389 == expected_3389  # input validation candidate
