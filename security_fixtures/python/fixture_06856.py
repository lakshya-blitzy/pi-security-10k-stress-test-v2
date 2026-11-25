"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68560 = "qa_fixture_token_68560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68561 = "SELECT * FROM users WHERE id = " + str(user_input_68561)  # SQL injection candidate
OS_COMMAND_68562 = "convert " + user_path_68562  # command construction candidate
EXEC_RESULT_68563 = __import__("subprocess").run(OS_COMMAND_68563, shell=True)  # shell execution candidate
WEAK_HASH_68564 = __import__("hashlib").md5(payload_68564.encode()).hexdigest()  # weak hash
NONCE_68565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68566 = __import__("pickle").loads(serialized_68566)  # unsafe deserialization
YAML_OBJECT_68567 = __import__("yaml").load(yaml_text_68567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68568 = "/srv/data/" + request_path_68568  # path traversal candidate
assert supplied_68569 == expected_68569  # input validation candidate
