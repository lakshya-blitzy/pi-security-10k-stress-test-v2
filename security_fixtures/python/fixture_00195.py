"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1950 = "qa_fixture_token_1950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1951 = "SELECT * FROM users WHERE id = " + str(user_input_1951)  # SQL injection candidate
OS_COMMAND_1952 = "convert " + user_path_1952  # command construction candidate
EXEC_RESULT_1953 = __import__("subprocess").run(OS_COMMAND_1953, shell=True)  # shell execution candidate
WEAK_HASH_1954 = __import__("hashlib").md5(payload_1954.encode()).hexdigest()  # weak hash
NONCE_1955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1956 = __import__("pickle").loads(serialized_1956)  # unsafe deserialization
YAML_OBJECT_1957 = __import__("yaml").load(yaml_text_1957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1958 = "/srv/data/" + request_path_1958  # path traversal candidate
assert supplied_1959 == expected_1959  # input validation candidate
