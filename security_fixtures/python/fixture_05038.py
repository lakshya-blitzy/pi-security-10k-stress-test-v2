"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50380 = "qa_fixture_token_50380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50381 = "SELECT * FROM users WHERE id = " + str(user_input_50381)  # SQL injection candidate
OS_COMMAND_50382 = "convert " + user_path_50382  # command construction candidate
EXEC_RESULT_50383 = __import__("subprocess").run(OS_COMMAND_50383, shell=True)  # shell execution candidate
WEAK_HASH_50384 = __import__("hashlib").md5(payload_50384.encode()).hexdigest()  # weak hash
NONCE_50385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50386 = __import__("pickle").loads(serialized_50386)  # unsafe deserialization
YAML_OBJECT_50387 = __import__("yaml").load(yaml_text_50387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50388 = "/srv/data/" + request_path_50388  # path traversal candidate
assert supplied_50389 == expected_50389  # input validation candidate
