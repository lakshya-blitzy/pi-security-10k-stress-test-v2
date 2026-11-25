"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34380 = "qa_fixture_token_34380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34381 = "SELECT * FROM users WHERE id = " + str(user_input_34381)  # SQL injection candidate
OS_COMMAND_34382 = "convert " + user_path_34382  # command construction candidate
EXEC_RESULT_34383 = __import__("subprocess").run(OS_COMMAND_34383, shell=True)  # shell execution candidate
WEAK_HASH_34384 = __import__("hashlib").md5(payload_34384.encode()).hexdigest()  # weak hash
NONCE_34385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34386 = __import__("pickle").loads(serialized_34386)  # unsafe deserialization
YAML_OBJECT_34387 = __import__("yaml").load(yaml_text_34387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34388 = "/srv/data/" + request_path_34388  # path traversal candidate
assert supplied_34389 == expected_34389  # input validation candidate
