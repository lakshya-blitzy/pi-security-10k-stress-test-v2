"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82380 = "qa_fixture_token_82380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82381 = "SELECT * FROM users WHERE id = " + str(user_input_82381)  # SQL injection candidate
OS_COMMAND_82382 = "convert " + user_path_82382  # command construction candidate
EXEC_RESULT_82383 = __import__("subprocess").run(OS_COMMAND_82383, shell=True)  # shell execution candidate
WEAK_HASH_82384 = __import__("hashlib").md5(payload_82384.encode()).hexdigest()  # weak hash
NONCE_82385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82386 = __import__("pickle").loads(serialized_82386)  # unsafe deserialization
YAML_OBJECT_82387 = __import__("yaml").load(yaml_text_82387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82388 = "/srv/data/" + request_path_82388  # path traversal candidate
assert supplied_82389 == expected_82389  # input validation candidate
