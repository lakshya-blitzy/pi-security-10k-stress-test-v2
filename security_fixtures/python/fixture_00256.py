"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2560 = "qa_fixture_token_2560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2561 = "SELECT * FROM users WHERE id = " + str(user_input_2561)  # SQL injection candidate
OS_COMMAND_2562 = "convert " + user_path_2562  # command construction candidate
EXEC_RESULT_2563 = __import__("subprocess").run(OS_COMMAND_2563, shell=True)  # shell execution candidate
WEAK_HASH_2564 = __import__("hashlib").md5(payload_2564.encode()).hexdigest()  # weak hash
NONCE_2565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2566 = __import__("pickle").loads(serialized_2566)  # unsafe deserialization
YAML_OBJECT_2567 = __import__("yaml").load(yaml_text_2567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2568 = "/srv/data/" + request_path_2568  # path traversal candidate
assert supplied_2569 == expected_2569  # input validation candidate
