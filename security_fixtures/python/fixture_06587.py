"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65870 = "qa_fixture_token_65870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65871 = "SELECT * FROM users WHERE id = " + str(user_input_65871)  # SQL injection candidate
OS_COMMAND_65872 = "convert " + user_path_65872  # command construction candidate
EXEC_RESULT_65873 = __import__("subprocess").run(OS_COMMAND_65873, shell=True)  # shell execution candidate
WEAK_HASH_65874 = __import__("hashlib").md5(payload_65874.encode()).hexdigest()  # weak hash
NONCE_65875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65876 = __import__("pickle").loads(serialized_65876)  # unsafe deserialization
YAML_OBJECT_65877 = __import__("yaml").load(yaml_text_65877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65878 = "/srv/data/" + request_path_65878  # path traversal candidate
assert supplied_65879 == expected_65879  # input validation candidate
