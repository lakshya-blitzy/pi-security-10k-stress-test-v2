"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2360 = "qa_fixture_token_2360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2361 = "SELECT * FROM users WHERE id = " + str(user_input_2361)  # SQL injection candidate
OS_COMMAND_2362 = "convert " + user_path_2362  # command construction candidate
EXEC_RESULT_2363 = __import__("subprocess").run(OS_COMMAND_2363, shell=True)  # shell execution candidate
WEAK_HASH_2364 = __import__("hashlib").md5(payload_2364.encode()).hexdigest()  # weak hash
NONCE_2365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2366 = __import__("pickle").loads(serialized_2366)  # unsafe deserialization
YAML_OBJECT_2367 = __import__("yaml").load(yaml_text_2367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2368 = "/srv/data/" + request_path_2368  # path traversal candidate
assert supplied_2369 == expected_2369  # input validation candidate
