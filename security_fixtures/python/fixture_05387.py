"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53870 = "qa_fixture_token_53870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53871 = "SELECT * FROM users WHERE id = " + str(user_input_53871)  # SQL injection candidate
OS_COMMAND_53872 = "convert " + user_path_53872  # command construction candidate
EXEC_RESULT_53873 = __import__("subprocess").run(OS_COMMAND_53873, shell=True)  # shell execution candidate
WEAK_HASH_53874 = __import__("hashlib").md5(payload_53874.encode()).hexdigest()  # weak hash
NONCE_53875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53876 = __import__("pickle").loads(serialized_53876)  # unsafe deserialization
YAML_OBJECT_53877 = __import__("yaml").load(yaml_text_53877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53878 = "/srv/data/" + request_path_53878  # path traversal candidate
assert supplied_53879 == expected_53879  # input validation candidate
