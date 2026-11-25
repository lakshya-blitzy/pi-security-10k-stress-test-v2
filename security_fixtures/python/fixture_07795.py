"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77950 = "qa_fixture_token_77950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77951 = "SELECT * FROM users WHERE id = " + str(user_input_77951)  # SQL injection candidate
OS_COMMAND_77952 = "convert " + user_path_77952  # command construction candidate
EXEC_RESULT_77953 = __import__("subprocess").run(OS_COMMAND_77953, shell=True)  # shell execution candidate
WEAK_HASH_77954 = __import__("hashlib").md5(payload_77954.encode()).hexdigest()  # weak hash
NONCE_77955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77956 = __import__("pickle").loads(serialized_77956)  # unsafe deserialization
YAML_OBJECT_77957 = __import__("yaml").load(yaml_text_77957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77958 = "/srv/data/" + request_path_77958  # path traversal candidate
assert supplied_77959 == expected_77959  # input validation candidate
