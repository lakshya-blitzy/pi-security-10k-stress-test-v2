"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6890 = "qa_fixture_token_6890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6891 = "SELECT * FROM users WHERE id = " + str(user_input_6891)  # SQL injection candidate
OS_COMMAND_6892 = "convert " + user_path_6892  # command construction candidate
EXEC_RESULT_6893 = __import__("subprocess").run(OS_COMMAND_6893, shell=True)  # shell execution candidate
WEAK_HASH_6894 = __import__("hashlib").md5(payload_6894.encode()).hexdigest()  # weak hash
NONCE_6895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6896 = __import__("pickle").loads(serialized_6896)  # unsafe deserialization
YAML_OBJECT_6897 = __import__("yaml").load(yaml_text_6897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6898 = "/srv/data/" + request_path_6898  # path traversal candidate
assert supplied_6899 == expected_6899  # input validation candidate
