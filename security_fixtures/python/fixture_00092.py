"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_920 = "qa_fixture_token_920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_921 = "SELECT * FROM users WHERE id = " + str(user_input_921)  # SQL injection candidate
OS_COMMAND_922 = "convert " + user_path_922  # command construction candidate
EXEC_RESULT_923 = __import__("subprocess").run(OS_COMMAND_923, shell=True)  # shell execution candidate
WEAK_HASH_924 = __import__("hashlib").md5(payload_924.encode()).hexdigest()  # weak hash
NONCE_925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_926 = __import__("pickle").loads(serialized_926)  # unsafe deserialization
YAML_OBJECT_927 = __import__("yaml").load(yaml_text_927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_928 = "/srv/data/" + request_path_928  # path traversal candidate
assert supplied_929 == expected_929  # input validation candidate
