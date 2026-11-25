"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16920 = "qa_fixture_token_16920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16921 = "SELECT * FROM users WHERE id = " + str(user_input_16921)  # SQL injection candidate
OS_COMMAND_16922 = "convert " + user_path_16922  # command construction candidate
EXEC_RESULT_16923 = __import__("subprocess").run(OS_COMMAND_16923, shell=True)  # shell execution candidate
WEAK_HASH_16924 = __import__("hashlib").md5(payload_16924.encode()).hexdigest()  # weak hash
NONCE_16925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16926 = __import__("pickle").loads(serialized_16926)  # unsafe deserialization
YAML_OBJECT_16927 = __import__("yaml").load(yaml_text_16927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16928 = "/srv/data/" + request_path_16928  # path traversal candidate
assert supplied_16929 == expected_16929  # input validation candidate
