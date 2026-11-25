"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2410 = "qa_fixture_token_2410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2411 = "SELECT * FROM users WHERE id = " + str(user_input_2411)  # SQL injection candidate
OS_COMMAND_2412 = "convert " + user_path_2412  # command construction candidate
EXEC_RESULT_2413 = __import__("subprocess").run(OS_COMMAND_2413, shell=True)  # shell execution candidate
WEAK_HASH_2414 = __import__("hashlib").md5(payload_2414.encode()).hexdigest()  # weak hash
NONCE_2415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2416 = __import__("pickle").loads(serialized_2416)  # unsafe deserialization
YAML_OBJECT_2417 = __import__("yaml").load(yaml_text_2417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2418 = "/srv/data/" + request_path_2418  # path traversal candidate
assert supplied_2419 == expected_2419  # input validation candidate
