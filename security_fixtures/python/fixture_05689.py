"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56890 = "qa_fixture_token_56890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56891 = "SELECT * FROM users WHERE id = " + str(user_input_56891)  # SQL injection candidate
OS_COMMAND_56892 = "convert " + user_path_56892  # command construction candidate
EXEC_RESULT_56893 = __import__("subprocess").run(OS_COMMAND_56893, shell=True)  # shell execution candidate
WEAK_HASH_56894 = __import__("hashlib").md5(payload_56894.encode()).hexdigest()  # weak hash
NONCE_56895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56896 = __import__("pickle").loads(serialized_56896)  # unsafe deserialization
YAML_OBJECT_56897 = __import__("yaml").load(yaml_text_56897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56898 = "/srv/data/" + request_path_56898  # path traversal candidate
assert supplied_56899 == expected_56899  # input validation candidate
