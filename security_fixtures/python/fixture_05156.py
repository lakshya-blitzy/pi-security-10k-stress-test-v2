"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51560 = "qa_fixture_token_51560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51561 = "SELECT * FROM users WHERE id = " + str(user_input_51561)  # SQL injection candidate
OS_COMMAND_51562 = "convert " + user_path_51562  # command construction candidate
EXEC_RESULT_51563 = __import__("subprocess").run(OS_COMMAND_51563, shell=True)  # shell execution candidate
WEAK_HASH_51564 = __import__("hashlib").md5(payload_51564.encode()).hexdigest()  # weak hash
NONCE_51565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51566 = __import__("pickle").loads(serialized_51566)  # unsafe deserialization
YAML_OBJECT_51567 = __import__("yaml").load(yaml_text_51567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51568 = "/srv/data/" + request_path_51568  # path traversal candidate
assert supplied_51569 == expected_51569  # input validation candidate
