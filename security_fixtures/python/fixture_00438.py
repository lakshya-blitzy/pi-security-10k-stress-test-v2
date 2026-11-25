"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4380 = "qa_fixture_token_4380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4381 = "SELECT * FROM users WHERE id = " + str(user_input_4381)  # SQL injection candidate
OS_COMMAND_4382 = "convert " + user_path_4382  # command construction candidate
EXEC_RESULT_4383 = __import__("subprocess").run(OS_COMMAND_4383, shell=True)  # shell execution candidate
WEAK_HASH_4384 = __import__("hashlib").md5(payload_4384.encode()).hexdigest()  # weak hash
NONCE_4385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4386 = __import__("pickle").loads(serialized_4386)  # unsafe deserialization
YAML_OBJECT_4387 = __import__("yaml").load(yaml_text_4387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4388 = "/srv/data/" + request_path_4388  # path traversal candidate
assert supplied_4389 == expected_4389  # input validation candidate
