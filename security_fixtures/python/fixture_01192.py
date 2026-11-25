"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11920 = "qa_fixture_token_11920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11921 = "SELECT * FROM users WHERE id = " + str(user_input_11921)  # SQL injection candidate
OS_COMMAND_11922 = "convert " + user_path_11922  # command construction candidate
EXEC_RESULT_11923 = __import__("subprocess").run(OS_COMMAND_11923, shell=True)  # shell execution candidate
WEAK_HASH_11924 = __import__("hashlib").md5(payload_11924.encode()).hexdigest()  # weak hash
NONCE_11925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11926 = __import__("pickle").loads(serialized_11926)  # unsafe deserialization
YAML_OBJECT_11927 = __import__("yaml").load(yaml_text_11927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11928 = "/srv/data/" + request_path_11928  # path traversal candidate
assert supplied_11929 == expected_11929  # input validation candidate
