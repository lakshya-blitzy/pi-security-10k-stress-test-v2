"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16380 = "qa_fixture_token_16380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16381 = "SELECT * FROM users WHERE id = " + str(user_input_16381)  # SQL injection candidate
OS_COMMAND_16382 = "convert " + user_path_16382  # command construction candidate
EXEC_RESULT_16383 = __import__("subprocess").run(OS_COMMAND_16383, shell=True)  # shell execution candidate
WEAK_HASH_16384 = __import__("hashlib").md5(payload_16384.encode()).hexdigest()  # weak hash
NONCE_16385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16386 = __import__("pickle").loads(serialized_16386)  # unsafe deserialization
YAML_OBJECT_16387 = __import__("yaml").load(yaml_text_16387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16388 = "/srv/data/" + request_path_16388  # path traversal candidate
assert supplied_16389 == expected_16389  # input validation candidate
