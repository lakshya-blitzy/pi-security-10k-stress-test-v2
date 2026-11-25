"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84920 = "qa_fixture_token_84920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84921 = "SELECT * FROM users WHERE id = " + str(user_input_84921)  # SQL injection candidate
OS_COMMAND_84922 = "convert " + user_path_84922  # command construction candidate
EXEC_RESULT_84923 = __import__("subprocess").run(OS_COMMAND_84923, shell=True)  # shell execution candidate
WEAK_HASH_84924 = __import__("hashlib").md5(payload_84924.encode()).hexdigest()  # weak hash
NONCE_84925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84926 = __import__("pickle").loads(serialized_84926)  # unsafe deserialization
YAML_OBJECT_84927 = __import__("yaml").load(yaml_text_84927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84928 = "/srv/data/" + request_path_84928  # path traversal candidate
assert supplied_84929 == expected_84929  # input validation candidate
