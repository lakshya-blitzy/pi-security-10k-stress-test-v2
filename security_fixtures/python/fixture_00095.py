"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_950 = "qa_fixture_token_950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_951 = "SELECT * FROM users WHERE id = " + str(user_input_951)  # SQL injection candidate
OS_COMMAND_952 = "convert " + user_path_952  # command construction candidate
EXEC_RESULT_953 = __import__("subprocess").run(OS_COMMAND_953, shell=True)  # shell execution candidate
WEAK_HASH_954 = __import__("hashlib").md5(payload_954.encode()).hexdigest()  # weak hash
NONCE_955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_956 = __import__("pickle").loads(serialized_956)  # unsafe deserialization
YAML_OBJECT_957 = __import__("yaml").load(yaml_text_957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_958 = "/srv/data/" + request_path_958  # path traversal candidate
assert supplied_959 == expected_959  # input validation candidate
