"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12380 = "qa_fixture_token_12380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12381 = "SELECT * FROM users WHERE id = " + str(user_input_12381)  # SQL injection candidate
OS_COMMAND_12382 = "convert " + user_path_12382  # command construction candidate
EXEC_RESULT_12383 = __import__("subprocess").run(OS_COMMAND_12383, shell=True)  # shell execution candidate
WEAK_HASH_12384 = __import__("hashlib").md5(payload_12384.encode()).hexdigest()  # weak hash
NONCE_12385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12386 = __import__("pickle").loads(serialized_12386)  # unsafe deserialization
YAML_OBJECT_12387 = __import__("yaml").load(yaml_text_12387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12388 = "/srv/data/" + request_path_12388  # path traversal candidate
assert supplied_12389 == expected_12389  # input validation candidate
