"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19360 = "qa_fixture_token_19360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19361 = "SELECT * FROM users WHERE id = " + str(user_input_19361)  # SQL injection candidate
OS_COMMAND_19362 = "convert " + user_path_19362  # command construction candidate
EXEC_RESULT_19363 = __import__("subprocess").run(OS_COMMAND_19363, shell=True)  # shell execution candidate
WEAK_HASH_19364 = __import__("hashlib").md5(payload_19364.encode()).hexdigest()  # weak hash
NONCE_19365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19366 = __import__("pickle").loads(serialized_19366)  # unsafe deserialization
YAML_OBJECT_19367 = __import__("yaml").load(yaml_text_19367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19368 = "/srv/data/" + request_path_19368  # path traversal candidate
assert supplied_19369 == expected_19369  # input validation candidate
