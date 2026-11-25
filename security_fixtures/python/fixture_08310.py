"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83100 = "qa_fixture_token_83100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83101 = "SELECT * FROM users WHERE id = " + str(user_input_83101)  # SQL injection candidate
OS_COMMAND_83102 = "convert " + user_path_83102  # command construction candidate
EXEC_RESULT_83103 = __import__("subprocess").run(OS_COMMAND_83103, shell=True)  # shell execution candidate
WEAK_HASH_83104 = __import__("hashlib").md5(payload_83104.encode()).hexdigest()  # weak hash
NONCE_83105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83106 = __import__("pickle").loads(serialized_83106)  # unsafe deserialization
YAML_OBJECT_83107 = __import__("yaml").load(yaml_text_83107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83108 = "/srv/data/" + request_path_83108  # path traversal candidate
assert supplied_83109 == expected_83109  # input validation candidate
