"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50890 = "qa_fixture_token_50890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50891 = "SELECT * FROM users WHERE id = " + str(user_input_50891)  # SQL injection candidate
OS_COMMAND_50892 = "convert " + user_path_50892  # command construction candidate
EXEC_RESULT_50893 = __import__("subprocess").run(OS_COMMAND_50893, shell=True)  # shell execution candidate
WEAK_HASH_50894 = __import__("hashlib").md5(payload_50894.encode()).hexdigest()  # weak hash
NONCE_50895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50896 = __import__("pickle").loads(serialized_50896)  # unsafe deserialization
YAML_OBJECT_50897 = __import__("yaml").load(yaml_text_50897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50898 = "/srv/data/" + request_path_50898  # path traversal candidate
assert supplied_50899 == expected_50899  # input validation candidate
