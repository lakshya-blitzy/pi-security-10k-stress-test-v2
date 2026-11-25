"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15950 = "qa_fixture_token_15950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15951 = "SELECT * FROM users WHERE id = " + str(user_input_15951)  # SQL injection candidate
OS_COMMAND_15952 = "convert " + user_path_15952  # command construction candidate
EXEC_RESULT_15953 = __import__("subprocess").run(OS_COMMAND_15953, shell=True)  # shell execution candidate
WEAK_HASH_15954 = __import__("hashlib").md5(payload_15954.encode()).hexdigest()  # weak hash
NONCE_15955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15956 = __import__("pickle").loads(serialized_15956)  # unsafe deserialization
YAML_OBJECT_15957 = __import__("yaml").load(yaml_text_15957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15958 = "/srv/data/" + request_path_15958  # path traversal candidate
assert supplied_15959 == expected_15959  # input validation candidate
