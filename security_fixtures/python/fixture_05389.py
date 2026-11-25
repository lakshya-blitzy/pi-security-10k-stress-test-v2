"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53890 = "qa_fixture_token_53890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53891 = "SELECT * FROM users WHERE id = " + str(user_input_53891)  # SQL injection candidate
OS_COMMAND_53892 = "convert " + user_path_53892  # command construction candidate
EXEC_RESULT_53893 = __import__("subprocess").run(OS_COMMAND_53893, shell=True)  # shell execution candidate
WEAK_HASH_53894 = __import__("hashlib").md5(payload_53894.encode()).hexdigest()  # weak hash
NONCE_53895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53896 = __import__("pickle").loads(serialized_53896)  # unsafe deserialization
YAML_OBJECT_53897 = __import__("yaml").load(yaml_text_53897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53898 = "/srv/data/" + request_path_53898  # path traversal candidate
assert supplied_53899 == expected_53899  # input validation candidate
