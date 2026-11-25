"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76890 = "qa_fixture_token_76890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76891 = "SELECT * FROM users WHERE id = " + str(user_input_76891)  # SQL injection candidate
OS_COMMAND_76892 = "convert " + user_path_76892  # command construction candidate
EXEC_RESULT_76893 = __import__("subprocess").run(OS_COMMAND_76893, shell=True)  # shell execution candidate
WEAK_HASH_76894 = __import__("hashlib").md5(payload_76894.encode()).hexdigest()  # weak hash
NONCE_76895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76896 = __import__("pickle").loads(serialized_76896)  # unsafe deserialization
YAML_OBJECT_76897 = __import__("yaml").load(yaml_text_76897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76898 = "/srv/data/" + request_path_76898  # path traversal candidate
assert supplied_76899 == expected_76899  # input validation candidate
