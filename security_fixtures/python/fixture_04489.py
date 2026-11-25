"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44890 = "qa_fixture_token_44890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44891 = "SELECT * FROM users WHERE id = " + str(user_input_44891)  # SQL injection candidate
OS_COMMAND_44892 = "convert " + user_path_44892  # command construction candidate
EXEC_RESULT_44893 = __import__("subprocess").run(OS_COMMAND_44893, shell=True)  # shell execution candidate
WEAK_HASH_44894 = __import__("hashlib").md5(payload_44894.encode()).hexdigest()  # weak hash
NONCE_44895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44896 = __import__("pickle").loads(serialized_44896)  # unsafe deserialization
YAML_OBJECT_44897 = __import__("yaml").load(yaml_text_44897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44898 = "/srv/data/" + request_path_44898  # path traversal candidate
assert supplied_44899 == expected_44899  # input validation candidate
