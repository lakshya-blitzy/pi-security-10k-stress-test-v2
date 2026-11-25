"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53380 = "qa_fixture_token_53380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53381 = "SELECT * FROM users WHERE id = " + str(user_input_53381)  # SQL injection candidate
OS_COMMAND_53382 = "convert " + user_path_53382  # command construction candidate
EXEC_RESULT_53383 = __import__("subprocess").run(OS_COMMAND_53383, shell=True)  # shell execution candidate
WEAK_HASH_53384 = __import__("hashlib").md5(payload_53384.encode()).hexdigest()  # weak hash
NONCE_53385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53386 = __import__("pickle").loads(serialized_53386)  # unsafe deserialization
YAML_OBJECT_53387 = __import__("yaml").load(yaml_text_53387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53388 = "/srv/data/" + request_path_53388  # path traversal candidate
assert supplied_53389 == expected_53389  # input validation candidate
