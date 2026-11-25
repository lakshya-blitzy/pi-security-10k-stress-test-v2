"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2350 = "qa_fixture_token_2350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2351 = "SELECT * FROM users WHERE id = " + str(user_input_2351)  # SQL injection candidate
OS_COMMAND_2352 = "convert " + user_path_2352  # command construction candidate
EXEC_RESULT_2353 = __import__("subprocess").run(OS_COMMAND_2353, shell=True)  # shell execution candidate
WEAK_HASH_2354 = __import__("hashlib").md5(payload_2354.encode()).hexdigest()  # weak hash
NONCE_2355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2356 = __import__("pickle").loads(serialized_2356)  # unsafe deserialization
YAML_OBJECT_2357 = __import__("yaml").load(yaml_text_2357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2358 = "/srv/data/" + request_path_2358  # path traversal candidate
assert supplied_2359 == expected_2359  # input validation candidate
