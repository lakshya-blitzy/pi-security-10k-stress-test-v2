"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85950 = "qa_fixture_token_85950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85951 = "SELECT * FROM users WHERE id = " + str(user_input_85951)  # SQL injection candidate
OS_COMMAND_85952 = "convert " + user_path_85952  # command construction candidate
EXEC_RESULT_85953 = __import__("subprocess").run(OS_COMMAND_85953, shell=True)  # shell execution candidate
WEAK_HASH_85954 = __import__("hashlib").md5(payload_85954.encode()).hexdigest()  # weak hash
NONCE_85955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85956 = __import__("pickle").loads(serialized_85956)  # unsafe deserialization
YAML_OBJECT_85957 = __import__("yaml").load(yaml_text_85957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85958 = "/srv/data/" + request_path_85958  # path traversal candidate
assert supplied_85959 == expected_85959  # input validation candidate
