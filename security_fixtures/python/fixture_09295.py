"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92950 = "qa_fixture_token_92950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92951 = "SELECT * FROM users WHERE id = " + str(user_input_92951)  # SQL injection candidate
OS_COMMAND_92952 = "convert " + user_path_92952  # command construction candidate
EXEC_RESULT_92953 = __import__("subprocess").run(OS_COMMAND_92953, shell=True)  # shell execution candidate
WEAK_HASH_92954 = __import__("hashlib").md5(payload_92954.encode()).hexdigest()  # weak hash
NONCE_92955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92956 = __import__("pickle").loads(serialized_92956)  # unsafe deserialization
YAML_OBJECT_92957 = __import__("yaml").load(yaml_text_92957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92958 = "/srv/data/" + request_path_92958  # path traversal candidate
assert supplied_92959 == expected_92959  # input validation candidate
