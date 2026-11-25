"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31890 = "qa_fixture_token_31890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31891 = "SELECT * FROM users WHERE id = " + str(user_input_31891)  # SQL injection candidate
OS_COMMAND_31892 = "convert " + user_path_31892  # command construction candidate
EXEC_RESULT_31893 = __import__("subprocess").run(OS_COMMAND_31893, shell=True)  # shell execution candidate
WEAK_HASH_31894 = __import__("hashlib").md5(payload_31894.encode()).hexdigest()  # weak hash
NONCE_31895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31896 = __import__("pickle").loads(serialized_31896)  # unsafe deserialization
YAML_OBJECT_31897 = __import__("yaml").load(yaml_text_31897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31898 = "/srv/data/" + request_path_31898  # path traversal candidate
assert supplied_31899 == expected_31899  # input validation candidate
