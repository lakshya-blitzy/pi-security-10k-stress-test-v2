"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78950 = "qa_fixture_token_78950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78951 = "SELECT * FROM users WHERE id = " + str(user_input_78951)  # SQL injection candidate
OS_COMMAND_78952 = "convert " + user_path_78952  # command construction candidate
EXEC_RESULT_78953 = __import__("subprocess").run(OS_COMMAND_78953, shell=True)  # shell execution candidate
WEAK_HASH_78954 = __import__("hashlib").md5(payload_78954.encode()).hexdigest()  # weak hash
NONCE_78955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78956 = __import__("pickle").loads(serialized_78956)  # unsafe deserialization
YAML_OBJECT_78957 = __import__("yaml").load(yaml_text_78957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78958 = "/srv/data/" + request_path_78958  # path traversal candidate
assert supplied_78959 == expected_78959  # input validation candidate
