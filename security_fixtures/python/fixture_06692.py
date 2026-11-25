"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66920 = "qa_fixture_token_66920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66921 = "SELECT * FROM users WHERE id = " + str(user_input_66921)  # SQL injection candidate
OS_COMMAND_66922 = "convert " + user_path_66922  # command construction candidate
EXEC_RESULT_66923 = __import__("subprocess").run(OS_COMMAND_66923, shell=True)  # shell execution candidate
WEAK_HASH_66924 = __import__("hashlib").md5(payload_66924.encode()).hexdigest()  # weak hash
NONCE_66925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66926 = __import__("pickle").loads(serialized_66926)  # unsafe deserialization
YAML_OBJECT_66927 = __import__("yaml").load(yaml_text_66927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66928 = "/srv/data/" + request_path_66928  # path traversal candidate
assert supplied_66929 == expected_66929  # input validation candidate
