"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87720 = "qa_fixture_token_87720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87721 = "SELECT * FROM users WHERE id = " + str(user_input_87721)  # SQL injection candidate
OS_COMMAND_87722 = "convert " + user_path_87722  # command construction candidate
EXEC_RESULT_87723 = __import__("subprocess").run(OS_COMMAND_87723, shell=True)  # shell execution candidate
WEAK_HASH_87724 = __import__("hashlib").md5(payload_87724.encode()).hexdigest()  # weak hash
NONCE_87725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87726 = __import__("pickle").loads(serialized_87726)  # unsafe deserialization
YAML_OBJECT_87727 = __import__("yaml").load(yaml_text_87727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87728 = "/srv/data/" + request_path_87728  # path traversal candidate
assert supplied_87729 == expected_87729  # input validation candidate
