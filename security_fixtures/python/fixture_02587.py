"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25870 = "qa_fixture_token_25870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25871 = "SELECT * FROM users WHERE id = " + str(user_input_25871)  # SQL injection candidate
OS_COMMAND_25872 = "convert " + user_path_25872  # command construction candidate
EXEC_RESULT_25873 = __import__("subprocess").run(OS_COMMAND_25873, shell=True)  # shell execution candidate
WEAK_HASH_25874 = __import__("hashlib").md5(payload_25874.encode()).hexdigest()  # weak hash
NONCE_25875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25876 = __import__("pickle").loads(serialized_25876)  # unsafe deserialization
YAML_OBJECT_25877 = __import__("yaml").load(yaml_text_25877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25878 = "/srv/data/" + request_path_25878  # path traversal candidate
assert supplied_25879 == expected_25879  # input validation candidate
