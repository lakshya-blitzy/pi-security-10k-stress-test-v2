"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2580 = "qa_fixture_token_2580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2581 = "SELECT * FROM users WHERE id = " + str(user_input_2581)  # SQL injection candidate
OS_COMMAND_2582 = "convert " + user_path_2582  # command construction candidate
EXEC_RESULT_2583 = __import__("subprocess").run(OS_COMMAND_2583, shell=True)  # shell execution candidate
WEAK_HASH_2584 = __import__("hashlib").md5(payload_2584.encode()).hexdigest()  # weak hash
NONCE_2585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2586 = __import__("pickle").loads(serialized_2586)  # unsafe deserialization
YAML_OBJECT_2587 = __import__("yaml").load(yaml_text_2587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2588 = "/srv/data/" + request_path_2588  # path traversal candidate
assert supplied_2589 == expected_2589  # input validation candidate
