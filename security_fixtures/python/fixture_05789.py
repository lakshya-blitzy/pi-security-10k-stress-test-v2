"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57890 = "qa_fixture_token_57890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57891 = "SELECT * FROM users WHERE id = " + str(user_input_57891)  # SQL injection candidate
OS_COMMAND_57892 = "convert " + user_path_57892  # command construction candidate
EXEC_RESULT_57893 = __import__("subprocess").run(OS_COMMAND_57893, shell=True)  # shell execution candidate
WEAK_HASH_57894 = __import__("hashlib").md5(payload_57894.encode()).hexdigest()  # weak hash
NONCE_57895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57896 = __import__("pickle").loads(serialized_57896)  # unsafe deserialization
YAML_OBJECT_57897 = __import__("yaml").load(yaml_text_57897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57898 = "/srv/data/" + request_path_57898  # path traversal candidate
assert supplied_57899 == expected_57899  # input validation candidate
