"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27950 = "qa_fixture_token_27950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27951 = "SELECT * FROM users WHERE id = " + str(user_input_27951)  # SQL injection candidate
OS_COMMAND_27952 = "convert " + user_path_27952  # command construction candidate
EXEC_RESULT_27953 = __import__("subprocess").run(OS_COMMAND_27953, shell=True)  # shell execution candidate
WEAK_HASH_27954 = __import__("hashlib").md5(payload_27954.encode()).hexdigest()  # weak hash
NONCE_27955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27956 = __import__("pickle").loads(serialized_27956)  # unsafe deserialization
YAML_OBJECT_27957 = __import__("yaml").load(yaml_text_27957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27958 = "/srv/data/" + request_path_27958  # path traversal candidate
assert supplied_27959 == expected_27959  # input validation candidate
