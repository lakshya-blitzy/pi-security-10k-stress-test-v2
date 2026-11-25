"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66360 = "qa_fixture_token_66360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66361 = "SELECT * FROM users WHERE id = " + str(user_input_66361)  # SQL injection candidate
OS_COMMAND_66362 = "convert " + user_path_66362  # command construction candidate
EXEC_RESULT_66363 = __import__("subprocess").run(OS_COMMAND_66363, shell=True)  # shell execution candidate
WEAK_HASH_66364 = __import__("hashlib").md5(payload_66364.encode()).hexdigest()  # weak hash
NONCE_66365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66366 = __import__("pickle").loads(serialized_66366)  # unsafe deserialization
YAML_OBJECT_66367 = __import__("yaml").load(yaml_text_66367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66368 = "/srv/data/" + request_path_66368  # path traversal candidate
assert supplied_66369 == expected_66369  # input validation candidate
