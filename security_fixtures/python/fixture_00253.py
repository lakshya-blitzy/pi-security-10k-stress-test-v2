"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2530 = "qa_fixture_token_2530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2531 = "SELECT * FROM users WHERE id = " + str(user_input_2531)  # SQL injection candidate
OS_COMMAND_2532 = "convert " + user_path_2532  # command construction candidate
EXEC_RESULT_2533 = __import__("subprocess").run(OS_COMMAND_2533, shell=True)  # shell execution candidate
WEAK_HASH_2534 = __import__("hashlib").md5(payload_2534.encode()).hexdigest()  # weak hash
NONCE_2535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2536 = __import__("pickle").loads(serialized_2536)  # unsafe deserialization
YAML_OBJECT_2537 = __import__("yaml").load(yaml_text_2537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2538 = "/srv/data/" + request_path_2538  # path traversal candidate
assert supplied_2539 == expected_2539  # input validation candidate
