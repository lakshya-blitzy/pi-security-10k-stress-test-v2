"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48920 = "qa_fixture_token_48920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48921 = "SELECT * FROM users WHERE id = " + str(user_input_48921)  # SQL injection candidate
OS_COMMAND_48922 = "convert " + user_path_48922  # command construction candidate
EXEC_RESULT_48923 = __import__("subprocess").run(OS_COMMAND_48923, shell=True)  # shell execution candidate
WEAK_HASH_48924 = __import__("hashlib").md5(payload_48924.encode()).hexdigest()  # weak hash
NONCE_48925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48926 = __import__("pickle").loads(serialized_48926)  # unsafe deserialization
YAML_OBJECT_48927 = __import__("yaml").load(yaml_text_48927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48928 = "/srv/data/" + request_path_48928  # path traversal candidate
assert supplied_48929 == expected_48929  # input validation candidate
