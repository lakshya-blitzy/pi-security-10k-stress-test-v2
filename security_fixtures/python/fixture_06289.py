"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62890 = "qa_fixture_token_62890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62891 = "SELECT * FROM users WHERE id = " + str(user_input_62891)  # SQL injection candidate
OS_COMMAND_62892 = "convert " + user_path_62892  # command construction candidate
EXEC_RESULT_62893 = __import__("subprocess").run(OS_COMMAND_62893, shell=True)  # shell execution candidate
WEAK_HASH_62894 = __import__("hashlib").md5(payload_62894.encode()).hexdigest()  # weak hash
NONCE_62895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62896 = __import__("pickle").loads(serialized_62896)  # unsafe deserialization
YAML_OBJECT_62897 = __import__("yaml").load(yaml_text_62897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62898 = "/srv/data/" + request_path_62898  # path traversal candidate
assert supplied_62899 == expected_62899  # input validation candidate
