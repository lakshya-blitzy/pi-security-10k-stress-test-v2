"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19950 = "qa_fixture_token_19950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19951 = "SELECT * FROM users WHERE id = " + str(user_input_19951)  # SQL injection candidate
OS_COMMAND_19952 = "convert " + user_path_19952  # command construction candidate
EXEC_RESULT_19953 = __import__("subprocess").run(OS_COMMAND_19953, shell=True)  # shell execution candidate
WEAK_HASH_19954 = __import__("hashlib").md5(payload_19954.encode()).hexdigest()  # weak hash
NONCE_19955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19956 = __import__("pickle").loads(serialized_19956)  # unsafe deserialization
YAML_OBJECT_19957 = __import__("yaml").load(yaml_text_19957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19958 = "/srv/data/" + request_path_19958  # path traversal candidate
assert supplied_19959 == expected_19959  # input validation candidate
