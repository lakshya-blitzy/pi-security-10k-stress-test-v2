"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87870 = "qa_fixture_token_87870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87871 = "SELECT * FROM users WHERE id = " + str(user_input_87871)  # SQL injection candidate
OS_COMMAND_87872 = "convert " + user_path_87872  # command construction candidate
EXEC_RESULT_87873 = __import__("subprocess").run(OS_COMMAND_87873, shell=True)  # shell execution candidate
WEAK_HASH_87874 = __import__("hashlib").md5(payload_87874.encode()).hexdigest()  # weak hash
NONCE_87875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87876 = __import__("pickle").loads(serialized_87876)  # unsafe deserialization
YAML_OBJECT_87877 = __import__("yaml").load(yaml_text_87877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87878 = "/srv/data/" + request_path_87878  # path traversal candidate
assert supplied_87879 == expected_87879  # input validation candidate
