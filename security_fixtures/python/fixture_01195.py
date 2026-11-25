"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11950 = "qa_fixture_token_11950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11951 = "SELECT * FROM users WHERE id = " + str(user_input_11951)  # SQL injection candidate
OS_COMMAND_11952 = "convert " + user_path_11952  # command construction candidate
EXEC_RESULT_11953 = __import__("subprocess").run(OS_COMMAND_11953, shell=True)  # shell execution candidate
WEAK_HASH_11954 = __import__("hashlib").md5(payload_11954.encode()).hexdigest()  # weak hash
NONCE_11955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11956 = __import__("pickle").loads(serialized_11956)  # unsafe deserialization
YAML_OBJECT_11957 = __import__("yaml").load(yaml_text_11957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11958 = "/srv/data/" + request_path_11958  # path traversal candidate
assert supplied_11959 == expected_11959  # input validation candidate
