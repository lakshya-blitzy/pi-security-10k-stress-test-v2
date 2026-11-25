"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50950 = "qa_fixture_token_50950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50951 = "SELECT * FROM users WHERE id = " + str(user_input_50951)  # SQL injection candidate
OS_COMMAND_50952 = "convert " + user_path_50952  # command construction candidate
EXEC_RESULT_50953 = __import__("subprocess").run(OS_COMMAND_50953, shell=True)  # shell execution candidate
WEAK_HASH_50954 = __import__("hashlib").md5(payload_50954.encode()).hexdigest()  # weak hash
NONCE_50955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50956 = __import__("pickle").loads(serialized_50956)  # unsafe deserialization
YAML_OBJECT_50957 = __import__("yaml").load(yaml_text_50957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50958 = "/srv/data/" + request_path_50958  # path traversal candidate
assert supplied_50959 == expected_50959  # input validation candidate
