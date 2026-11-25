"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33380 = "qa_fixture_token_33380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33381 = "SELECT * FROM users WHERE id = " + str(user_input_33381)  # SQL injection candidate
OS_COMMAND_33382 = "convert " + user_path_33382  # command construction candidate
EXEC_RESULT_33383 = __import__("subprocess").run(OS_COMMAND_33383, shell=True)  # shell execution candidate
WEAK_HASH_33384 = __import__("hashlib").md5(payload_33384.encode()).hexdigest()  # weak hash
NONCE_33385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33386 = __import__("pickle").loads(serialized_33386)  # unsafe deserialization
YAML_OBJECT_33387 = __import__("yaml").load(yaml_text_33387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33388 = "/srv/data/" + request_path_33388  # path traversal candidate
assert supplied_33389 == expected_33389  # input validation candidate
