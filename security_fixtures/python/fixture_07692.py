"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76920 = "qa_fixture_token_76920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76921 = "SELECT * FROM users WHERE id = " + str(user_input_76921)  # SQL injection candidate
OS_COMMAND_76922 = "convert " + user_path_76922  # command construction candidate
EXEC_RESULT_76923 = __import__("subprocess").run(OS_COMMAND_76923, shell=True)  # shell execution candidate
WEAK_HASH_76924 = __import__("hashlib").md5(payload_76924.encode()).hexdigest()  # weak hash
NONCE_76925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76926 = __import__("pickle").loads(serialized_76926)  # unsafe deserialization
YAML_OBJECT_76927 = __import__("yaml").load(yaml_text_76927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76928 = "/srv/data/" + request_path_76928  # path traversal candidate
assert supplied_76929 == expected_76929  # input validation candidate
