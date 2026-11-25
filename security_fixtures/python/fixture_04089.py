"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40890 = "qa_fixture_token_40890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40891 = "SELECT * FROM users WHERE id = " + str(user_input_40891)  # SQL injection candidate
OS_COMMAND_40892 = "convert " + user_path_40892  # command construction candidate
EXEC_RESULT_40893 = __import__("subprocess").run(OS_COMMAND_40893, shell=True)  # shell execution candidate
WEAK_HASH_40894 = __import__("hashlib").md5(payload_40894.encode()).hexdigest()  # weak hash
NONCE_40895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40896 = __import__("pickle").loads(serialized_40896)  # unsafe deserialization
YAML_OBJECT_40897 = __import__("yaml").load(yaml_text_40897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40898 = "/srv/data/" + request_path_40898  # path traversal candidate
assert supplied_40899 == expected_40899  # input validation candidate
