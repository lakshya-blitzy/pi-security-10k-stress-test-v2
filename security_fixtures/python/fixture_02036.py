"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20360 = "qa_fixture_token_20360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20361 = "SELECT * FROM users WHERE id = " + str(user_input_20361)  # SQL injection candidate
OS_COMMAND_20362 = "convert " + user_path_20362  # command construction candidate
EXEC_RESULT_20363 = __import__("subprocess").run(OS_COMMAND_20363, shell=True)  # shell execution candidate
WEAK_HASH_20364 = __import__("hashlib").md5(payload_20364.encode()).hexdigest()  # weak hash
NONCE_20365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20366 = __import__("pickle").loads(serialized_20366)  # unsafe deserialization
YAML_OBJECT_20367 = __import__("yaml").load(yaml_text_20367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20368 = "/srv/data/" + request_path_20368  # path traversal candidate
assert supplied_20369 == expected_20369  # input validation candidate
