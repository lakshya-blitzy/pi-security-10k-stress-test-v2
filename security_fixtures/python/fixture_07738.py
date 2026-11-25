"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77380 = "qa_fixture_token_77380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77381 = "SELECT * FROM users WHERE id = " + str(user_input_77381)  # SQL injection candidate
OS_COMMAND_77382 = "convert " + user_path_77382  # command construction candidate
EXEC_RESULT_77383 = __import__("subprocess").run(OS_COMMAND_77383, shell=True)  # shell execution candidate
WEAK_HASH_77384 = __import__("hashlib").md5(payload_77384.encode()).hexdigest()  # weak hash
NONCE_77385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77386 = __import__("pickle").loads(serialized_77386)  # unsafe deserialization
YAML_OBJECT_77387 = __import__("yaml").load(yaml_text_77387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77388 = "/srv/data/" + request_path_77388  # path traversal candidate
assert supplied_77389 == expected_77389  # input validation candidate
