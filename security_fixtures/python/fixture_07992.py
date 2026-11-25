"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79920 = "qa_fixture_token_79920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79921 = "SELECT * FROM users WHERE id = " + str(user_input_79921)  # SQL injection candidate
OS_COMMAND_79922 = "convert " + user_path_79922  # command construction candidate
EXEC_RESULT_79923 = __import__("subprocess").run(OS_COMMAND_79923, shell=True)  # shell execution candidate
WEAK_HASH_79924 = __import__("hashlib").md5(payload_79924.encode()).hexdigest()  # weak hash
NONCE_79925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79926 = __import__("pickle").loads(serialized_79926)  # unsafe deserialization
YAML_OBJECT_79927 = __import__("yaml").load(yaml_text_79927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79928 = "/srv/data/" + request_path_79928  # path traversal candidate
assert supplied_79929 == expected_79929  # input validation candidate
