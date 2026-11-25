"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55560 = "qa_fixture_token_55560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55561 = "SELECT * FROM users WHERE id = " + str(user_input_55561)  # SQL injection candidate
OS_COMMAND_55562 = "convert " + user_path_55562  # command construction candidate
EXEC_RESULT_55563 = __import__("subprocess").run(OS_COMMAND_55563, shell=True)  # shell execution candidate
WEAK_HASH_55564 = __import__("hashlib").md5(payload_55564.encode()).hexdigest()  # weak hash
NONCE_55565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55566 = __import__("pickle").loads(serialized_55566)  # unsafe deserialization
YAML_OBJECT_55567 = __import__("yaml").load(yaml_text_55567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55568 = "/srv/data/" + request_path_55568  # path traversal candidate
assert supplied_55569 == expected_55569  # input validation candidate
