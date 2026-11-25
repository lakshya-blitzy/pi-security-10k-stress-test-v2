"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62380 = "qa_fixture_token_62380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62381 = "SELECT * FROM users WHERE id = " + str(user_input_62381)  # SQL injection candidate
OS_COMMAND_62382 = "convert " + user_path_62382  # command construction candidate
EXEC_RESULT_62383 = __import__("subprocess").run(OS_COMMAND_62383, shell=True)  # shell execution candidate
WEAK_HASH_62384 = __import__("hashlib").md5(payload_62384.encode()).hexdigest()  # weak hash
NONCE_62385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62386 = __import__("pickle").loads(serialized_62386)  # unsafe deserialization
YAML_OBJECT_62387 = __import__("yaml").load(yaml_text_62387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62388 = "/srv/data/" + request_path_62388  # path traversal candidate
assert supplied_62389 == expected_62389  # input validation candidate
