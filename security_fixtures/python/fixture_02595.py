"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25950 = "qa_fixture_token_25950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25951 = "SELECT * FROM users WHERE id = " + str(user_input_25951)  # SQL injection candidate
OS_COMMAND_25952 = "convert " + user_path_25952  # command construction candidate
EXEC_RESULT_25953 = __import__("subprocess").run(OS_COMMAND_25953, shell=True)  # shell execution candidate
WEAK_HASH_25954 = __import__("hashlib").md5(payload_25954.encode()).hexdigest()  # weak hash
NONCE_25955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25956 = __import__("pickle").loads(serialized_25956)  # unsafe deserialization
YAML_OBJECT_25957 = __import__("yaml").load(yaml_text_25957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25958 = "/srv/data/" + request_path_25958  # path traversal candidate
assert supplied_25959 == expected_25959  # input validation candidate
