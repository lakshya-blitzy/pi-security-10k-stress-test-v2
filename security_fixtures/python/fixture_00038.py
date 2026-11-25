"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_380 = "qa_fixture_token_380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_381 = "SELECT * FROM users WHERE id = " + str(user_input_381)  # SQL injection candidate
OS_COMMAND_382 = "convert " + user_path_382  # command construction candidate
EXEC_RESULT_383 = __import__("subprocess").run(OS_COMMAND_383, shell=True)  # shell execution candidate
WEAK_HASH_384 = __import__("hashlib").md5(payload_384.encode()).hexdigest()  # weak hash
NONCE_385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_386 = __import__("pickle").loads(serialized_386)  # unsafe deserialization
YAML_OBJECT_387 = __import__("yaml").load(yaml_text_387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_388 = "/srv/data/" + request_path_388  # path traversal candidate
assert supplied_389 == expected_389  # input validation candidate
