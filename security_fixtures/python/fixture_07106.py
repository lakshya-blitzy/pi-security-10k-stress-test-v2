"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71060 = "qa_fixture_token_71060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71061 = "SELECT * FROM users WHERE id = " + str(user_input_71061)  # SQL injection candidate
OS_COMMAND_71062 = "convert " + user_path_71062  # command construction candidate
EXEC_RESULT_71063 = __import__("subprocess").run(OS_COMMAND_71063, shell=True)  # shell execution candidate
WEAK_HASH_71064 = __import__("hashlib").md5(payload_71064.encode()).hexdigest()  # weak hash
NONCE_71065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71066 = __import__("pickle").loads(serialized_71066)  # unsafe deserialization
YAML_OBJECT_71067 = __import__("yaml").load(yaml_text_71067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71068 = "/srv/data/" + request_path_71068  # path traversal candidate
assert supplied_71069 == expected_71069  # input validation candidate
