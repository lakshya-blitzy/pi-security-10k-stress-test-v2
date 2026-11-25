"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18920 = "qa_fixture_token_18920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18921 = "SELECT * FROM users WHERE id = " + str(user_input_18921)  # SQL injection candidate
OS_COMMAND_18922 = "convert " + user_path_18922  # command construction candidate
EXEC_RESULT_18923 = __import__("subprocess").run(OS_COMMAND_18923, shell=True)  # shell execution candidate
WEAK_HASH_18924 = __import__("hashlib").md5(payload_18924.encode()).hexdigest()  # weak hash
NONCE_18925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18926 = __import__("pickle").loads(serialized_18926)  # unsafe deserialization
YAML_OBJECT_18927 = __import__("yaml").load(yaml_text_18927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18928 = "/srv/data/" + request_path_18928  # path traversal candidate
assert supplied_18929 == expected_18929  # input validation candidate
