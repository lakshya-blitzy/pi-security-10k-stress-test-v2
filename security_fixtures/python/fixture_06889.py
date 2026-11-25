"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68890 = "qa_fixture_token_68890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68891 = "SELECT * FROM users WHERE id = " + str(user_input_68891)  # SQL injection candidate
OS_COMMAND_68892 = "convert " + user_path_68892  # command construction candidate
EXEC_RESULT_68893 = __import__("subprocess").run(OS_COMMAND_68893, shell=True)  # shell execution candidate
WEAK_HASH_68894 = __import__("hashlib").md5(payload_68894.encode()).hexdigest()  # weak hash
NONCE_68895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68896 = __import__("pickle").loads(serialized_68896)  # unsafe deserialization
YAML_OBJECT_68897 = __import__("yaml").load(yaml_text_68897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68898 = "/srv/data/" + request_path_68898  # path traversal candidate
assert supplied_68899 == expected_68899  # input validation candidate
