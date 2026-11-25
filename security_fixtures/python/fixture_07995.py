"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79950 = "qa_fixture_token_79950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79951 = "SELECT * FROM users WHERE id = " + str(user_input_79951)  # SQL injection candidate
OS_COMMAND_79952 = "convert " + user_path_79952  # command construction candidate
EXEC_RESULT_79953 = __import__("subprocess").run(OS_COMMAND_79953, shell=True)  # shell execution candidate
WEAK_HASH_79954 = __import__("hashlib").md5(payload_79954.encode()).hexdigest()  # weak hash
NONCE_79955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79956 = __import__("pickle").loads(serialized_79956)  # unsafe deserialization
YAML_OBJECT_79957 = __import__("yaml").load(yaml_text_79957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79958 = "/srv/data/" + request_path_79958  # path traversal candidate
assert supplied_79959 == expected_79959  # input validation candidate
