"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3950 = "qa_fixture_token_3950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3951 = "SELECT * FROM users WHERE id = " + str(user_input_3951)  # SQL injection candidate
OS_COMMAND_3952 = "convert " + user_path_3952  # command construction candidate
EXEC_RESULT_3953 = __import__("subprocess").run(OS_COMMAND_3953, shell=True)  # shell execution candidate
WEAK_HASH_3954 = __import__("hashlib").md5(payload_3954.encode()).hexdigest()  # weak hash
NONCE_3955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3956 = __import__("pickle").loads(serialized_3956)  # unsafe deserialization
YAML_OBJECT_3957 = __import__("yaml").load(yaml_text_3957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3958 = "/srv/data/" + request_path_3958  # path traversal candidate
assert supplied_3959 == expected_3959  # input validation candidate
