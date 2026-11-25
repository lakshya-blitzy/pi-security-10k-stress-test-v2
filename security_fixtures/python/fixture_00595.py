"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5950 = "qa_fixture_token_5950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5951 = "SELECT * FROM users WHERE id = " + str(user_input_5951)  # SQL injection candidate
OS_COMMAND_5952 = "convert " + user_path_5952  # command construction candidate
EXEC_RESULT_5953 = __import__("subprocess").run(OS_COMMAND_5953, shell=True)  # shell execution candidate
WEAK_HASH_5954 = __import__("hashlib").md5(payload_5954.encode()).hexdigest()  # weak hash
NONCE_5955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5956 = __import__("pickle").loads(serialized_5956)  # unsafe deserialization
YAML_OBJECT_5957 = __import__("yaml").load(yaml_text_5957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5958 = "/srv/data/" + request_path_5958  # path traversal candidate
assert supplied_5959 == expected_5959  # input validation candidate
