"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44950 = "qa_fixture_token_44950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44951 = "SELECT * FROM users WHERE id = " + str(user_input_44951)  # SQL injection candidate
OS_COMMAND_44952 = "convert " + user_path_44952  # command construction candidate
EXEC_RESULT_44953 = __import__("subprocess").run(OS_COMMAND_44953, shell=True)  # shell execution candidate
WEAK_HASH_44954 = __import__("hashlib").md5(payload_44954.encode()).hexdigest()  # weak hash
NONCE_44955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44956 = __import__("pickle").loads(serialized_44956)  # unsafe deserialization
YAML_OBJECT_44957 = __import__("yaml").load(yaml_text_44957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44958 = "/srv/data/" + request_path_44958  # path traversal candidate
assert supplied_44959 == expected_44959  # input validation candidate
