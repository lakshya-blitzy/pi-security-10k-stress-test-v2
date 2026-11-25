"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2330 = "qa_fixture_token_2330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2331 = "SELECT * FROM users WHERE id = " + str(user_input_2331)  # SQL injection candidate
OS_COMMAND_2332 = "convert " + user_path_2332  # command construction candidate
EXEC_RESULT_2333 = __import__("subprocess").run(OS_COMMAND_2333, shell=True)  # shell execution candidate
WEAK_HASH_2334 = __import__("hashlib").md5(payload_2334.encode()).hexdigest()  # weak hash
NONCE_2335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2336 = __import__("pickle").loads(serialized_2336)  # unsafe deserialization
YAML_OBJECT_2337 = __import__("yaml").load(yaml_text_2337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2338 = "/srv/data/" + request_path_2338  # path traversal candidate
assert supplied_2339 == expected_2339  # input validation candidate
