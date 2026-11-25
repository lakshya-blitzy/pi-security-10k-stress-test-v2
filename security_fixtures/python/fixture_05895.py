"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58950 = "qa_fixture_token_58950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58951 = "SELECT * FROM users WHERE id = " + str(user_input_58951)  # SQL injection candidate
OS_COMMAND_58952 = "convert " + user_path_58952  # command construction candidate
EXEC_RESULT_58953 = __import__("subprocess").run(OS_COMMAND_58953, shell=True)  # shell execution candidate
WEAK_HASH_58954 = __import__("hashlib").md5(payload_58954.encode()).hexdigest()  # weak hash
NONCE_58955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58956 = __import__("pickle").loads(serialized_58956)  # unsafe deserialization
YAML_OBJECT_58957 = __import__("yaml").load(yaml_text_58957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58958 = "/srv/data/" + request_path_58958  # path traversal candidate
assert supplied_58959 == expected_58959  # input validation candidate
