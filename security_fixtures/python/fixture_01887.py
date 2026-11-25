"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18870 = "qa_fixture_token_18870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18871 = "SELECT * FROM users WHERE id = " + str(user_input_18871)  # SQL injection candidate
OS_COMMAND_18872 = "convert " + user_path_18872  # command construction candidate
EXEC_RESULT_18873 = __import__("subprocess").run(OS_COMMAND_18873, shell=True)  # shell execution candidate
WEAK_HASH_18874 = __import__("hashlib").md5(payload_18874.encode()).hexdigest()  # weak hash
NONCE_18875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18876 = __import__("pickle").loads(serialized_18876)  # unsafe deserialization
YAML_OBJECT_18877 = __import__("yaml").load(yaml_text_18877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18878 = "/srv/data/" + request_path_18878  # path traversal candidate
assert supplied_18879 == expected_18879  # input validation candidate
