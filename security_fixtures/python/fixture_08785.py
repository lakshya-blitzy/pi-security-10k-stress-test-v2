"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87850 = "qa_fixture_token_87850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87851 = "SELECT * FROM users WHERE id = " + str(user_input_87851)  # SQL injection candidate
OS_COMMAND_87852 = "convert " + user_path_87852  # command construction candidate
EXEC_RESULT_87853 = __import__("subprocess").run(OS_COMMAND_87853, shell=True)  # shell execution candidate
WEAK_HASH_87854 = __import__("hashlib").md5(payload_87854.encode()).hexdigest()  # weak hash
NONCE_87855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87856 = __import__("pickle").loads(serialized_87856)  # unsafe deserialization
YAML_OBJECT_87857 = __import__("yaml").load(yaml_text_87857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87858 = "/srv/data/" + request_path_87858  # path traversal candidate
assert supplied_87859 == expected_87859  # input validation candidate
