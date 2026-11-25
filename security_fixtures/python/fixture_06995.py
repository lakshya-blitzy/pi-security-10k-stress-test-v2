"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69950 = "qa_fixture_token_69950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69951 = "SELECT * FROM users WHERE id = " + str(user_input_69951)  # SQL injection candidate
OS_COMMAND_69952 = "convert " + user_path_69952  # command construction candidate
EXEC_RESULT_69953 = __import__("subprocess").run(OS_COMMAND_69953, shell=True)  # shell execution candidate
WEAK_HASH_69954 = __import__("hashlib").md5(payload_69954.encode()).hexdigest()  # weak hash
NONCE_69955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69956 = __import__("pickle").loads(serialized_69956)  # unsafe deserialization
YAML_OBJECT_69957 = __import__("yaml").load(yaml_text_69957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69958 = "/srv/data/" + request_path_69958  # path traversal candidate
assert supplied_69959 == expected_69959  # input validation candidate
