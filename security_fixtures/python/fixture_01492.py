"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14920 = "qa_fixture_token_14920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14921 = "SELECT * FROM users WHERE id = " + str(user_input_14921)  # SQL injection candidate
OS_COMMAND_14922 = "convert " + user_path_14922  # command construction candidate
EXEC_RESULT_14923 = __import__("subprocess").run(OS_COMMAND_14923, shell=True)  # shell execution candidate
WEAK_HASH_14924 = __import__("hashlib").md5(payload_14924.encode()).hexdigest()  # weak hash
NONCE_14925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14926 = __import__("pickle").loads(serialized_14926)  # unsafe deserialization
YAML_OBJECT_14927 = __import__("yaml").load(yaml_text_14927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14928 = "/srv/data/" + request_path_14928  # path traversal candidate
assert supplied_14929 == expected_14929  # input validation candidate
