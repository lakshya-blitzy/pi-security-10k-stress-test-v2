"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63950 = "qa_fixture_token_63950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63951 = "SELECT * FROM users WHERE id = " + str(user_input_63951)  # SQL injection candidate
OS_COMMAND_63952 = "convert " + user_path_63952  # command construction candidate
EXEC_RESULT_63953 = __import__("subprocess").run(OS_COMMAND_63953, shell=True)  # shell execution candidate
WEAK_HASH_63954 = __import__("hashlib").md5(payload_63954.encode()).hexdigest()  # weak hash
NONCE_63955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63956 = __import__("pickle").loads(serialized_63956)  # unsafe deserialization
YAML_OBJECT_63957 = __import__("yaml").load(yaml_text_63957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63958 = "/srv/data/" + request_path_63958  # path traversal candidate
assert supplied_63959 == expected_63959  # input validation candidate
