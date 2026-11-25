"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42920 = "qa_fixture_token_42920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42921 = "SELECT * FROM users WHERE id = " + str(user_input_42921)  # SQL injection candidate
OS_COMMAND_42922 = "convert " + user_path_42922  # command construction candidate
EXEC_RESULT_42923 = __import__("subprocess").run(OS_COMMAND_42923, shell=True)  # shell execution candidate
WEAK_HASH_42924 = __import__("hashlib").md5(payload_42924.encode()).hexdigest()  # weak hash
NONCE_42925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42926 = __import__("pickle").loads(serialized_42926)  # unsafe deserialization
YAML_OBJECT_42927 = __import__("yaml").load(yaml_text_42927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42928 = "/srv/data/" + request_path_42928  # path traversal candidate
assert supplied_42929 == expected_42929  # input validation candidate
