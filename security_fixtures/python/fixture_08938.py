"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89380 = "qa_fixture_token_89380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89381 = "SELECT * FROM users WHERE id = " + str(user_input_89381)  # SQL injection candidate
OS_COMMAND_89382 = "convert " + user_path_89382  # command construction candidate
EXEC_RESULT_89383 = __import__("subprocess").run(OS_COMMAND_89383, shell=True)  # shell execution candidate
WEAK_HASH_89384 = __import__("hashlib").md5(payload_89384.encode()).hexdigest()  # weak hash
NONCE_89385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89386 = __import__("pickle").loads(serialized_89386)  # unsafe deserialization
YAML_OBJECT_89387 = __import__("yaml").load(yaml_text_89387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89388 = "/srv/data/" + request_path_89388  # path traversal candidate
assert supplied_89389 == expected_89389  # input validation candidate
