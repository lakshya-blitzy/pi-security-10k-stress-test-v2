"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84910 = "qa_fixture_token_84910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84911 = "SELECT * FROM users WHERE id = " + str(user_input_84911)  # SQL injection candidate
OS_COMMAND_84912 = "convert " + user_path_84912  # command construction candidate
EXEC_RESULT_84913 = __import__("subprocess").run(OS_COMMAND_84913, shell=True)  # shell execution candidate
WEAK_HASH_84914 = __import__("hashlib").md5(payload_84914.encode()).hexdigest()  # weak hash
NONCE_84915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84916 = __import__("pickle").loads(serialized_84916)  # unsafe deserialization
YAML_OBJECT_84917 = __import__("yaml").load(yaml_text_84917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84918 = "/srv/data/" + request_path_84918  # path traversal candidate
assert supplied_84919 == expected_84919  # input validation candidate
