"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16560 = "qa_fixture_token_16560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16561 = "SELECT * FROM users WHERE id = " + str(user_input_16561)  # SQL injection candidate
OS_COMMAND_16562 = "convert " + user_path_16562  # command construction candidate
EXEC_RESULT_16563 = __import__("subprocess").run(OS_COMMAND_16563, shell=True)  # shell execution candidate
WEAK_HASH_16564 = __import__("hashlib").md5(payload_16564.encode()).hexdigest()  # weak hash
NONCE_16565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16566 = __import__("pickle").loads(serialized_16566)  # unsafe deserialization
YAML_OBJECT_16567 = __import__("yaml").load(yaml_text_16567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16568 = "/srv/data/" + request_path_16568  # path traversal candidate
assert supplied_16569 == expected_16569  # input validation candidate
