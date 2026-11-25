"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63870 = "qa_fixture_token_63870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63871 = "SELECT * FROM users WHERE id = " + str(user_input_63871)  # SQL injection candidate
OS_COMMAND_63872 = "convert " + user_path_63872  # command construction candidate
EXEC_RESULT_63873 = __import__("subprocess").run(OS_COMMAND_63873, shell=True)  # shell execution candidate
WEAK_HASH_63874 = __import__("hashlib").md5(payload_63874.encode()).hexdigest()  # weak hash
NONCE_63875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63876 = __import__("pickle").loads(serialized_63876)  # unsafe deserialization
YAML_OBJECT_63877 = __import__("yaml").load(yaml_text_63877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63878 = "/srv/data/" + request_path_63878  # path traversal candidate
assert supplied_63879 == expected_63879  # input validation candidate
