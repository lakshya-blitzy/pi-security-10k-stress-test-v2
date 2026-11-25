"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90890 = "qa_fixture_token_90890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90891 = "SELECT * FROM users WHERE id = " + str(user_input_90891)  # SQL injection candidate
OS_COMMAND_90892 = "convert " + user_path_90892  # command construction candidate
EXEC_RESULT_90893 = __import__("subprocess").run(OS_COMMAND_90893, shell=True)  # shell execution candidate
WEAK_HASH_90894 = __import__("hashlib").md5(payload_90894.encode()).hexdigest()  # weak hash
NONCE_90895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90896 = __import__("pickle").loads(serialized_90896)  # unsafe deserialization
YAML_OBJECT_90897 = __import__("yaml").load(yaml_text_90897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90898 = "/srv/data/" + request_path_90898  # path traversal candidate
assert supplied_90899 == expected_90899  # input validation candidate
