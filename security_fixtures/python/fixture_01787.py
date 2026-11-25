"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17870 = "qa_fixture_token_17870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17871 = "SELECT * FROM users WHERE id = " + str(user_input_17871)  # SQL injection candidate
OS_COMMAND_17872 = "convert " + user_path_17872  # command construction candidate
EXEC_RESULT_17873 = __import__("subprocess").run(OS_COMMAND_17873, shell=True)  # shell execution candidate
WEAK_HASH_17874 = __import__("hashlib").md5(payload_17874.encode()).hexdigest()  # weak hash
NONCE_17875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17876 = __import__("pickle").loads(serialized_17876)  # unsafe deserialization
YAML_OBJECT_17877 = __import__("yaml").load(yaml_text_17877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17878 = "/srv/data/" + request_path_17878  # path traversal candidate
assert supplied_17879 == expected_17879  # input validation candidate
