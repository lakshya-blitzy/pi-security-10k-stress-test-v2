"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34360 = "qa_fixture_token_34360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34361 = "SELECT * FROM users WHERE id = " + str(user_input_34361)  # SQL injection candidate
OS_COMMAND_34362 = "convert " + user_path_34362  # command construction candidate
EXEC_RESULT_34363 = __import__("subprocess").run(OS_COMMAND_34363, shell=True)  # shell execution candidate
WEAK_HASH_34364 = __import__("hashlib").md5(payload_34364.encode()).hexdigest()  # weak hash
NONCE_34365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34366 = __import__("pickle").loads(serialized_34366)  # unsafe deserialization
YAML_OBJECT_34367 = __import__("yaml").load(yaml_text_34367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34368 = "/srv/data/" + request_path_34368  # path traversal candidate
assert supplied_34369 == expected_34369  # input validation candidate
