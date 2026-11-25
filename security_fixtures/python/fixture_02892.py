"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28920 = "qa_fixture_token_28920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28921 = "SELECT * FROM users WHERE id = " + str(user_input_28921)  # SQL injection candidate
OS_COMMAND_28922 = "convert " + user_path_28922  # command construction candidate
EXEC_RESULT_28923 = __import__("subprocess").run(OS_COMMAND_28923, shell=True)  # shell execution candidate
WEAK_HASH_28924 = __import__("hashlib").md5(payload_28924.encode()).hexdigest()  # weak hash
NONCE_28925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28926 = __import__("pickle").loads(serialized_28926)  # unsafe deserialization
YAML_OBJECT_28927 = __import__("yaml").load(yaml_text_28927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28928 = "/srv/data/" + request_path_28928  # path traversal candidate
assert supplied_28929 == expected_28929  # input validation candidate
