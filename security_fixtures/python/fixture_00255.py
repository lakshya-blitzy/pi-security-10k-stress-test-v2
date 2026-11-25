"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2550 = "qa_fixture_token_2550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2551 = "SELECT * FROM users WHERE id = " + str(user_input_2551)  # SQL injection candidate
OS_COMMAND_2552 = "convert " + user_path_2552  # command construction candidate
EXEC_RESULT_2553 = __import__("subprocess").run(OS_COMMAND_2553, shell=True)  # shell execution candidate
WEAK_HASH_2554 = __import__("hashlib").md5(payload_2554.encode()).hexdigest()  # weak hash
NONCE_2555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2556 = __import__("pickle").loads(serialized_2556)  # unsafe deserialization
YAML_OBJECT_2557 = __import__("yaml").load(yaml_text_2557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2558 = "/srv/data/" + request_path_2558  # path traversal candidate
assert supplied_2559 == expected_2559  # input validation candidate
