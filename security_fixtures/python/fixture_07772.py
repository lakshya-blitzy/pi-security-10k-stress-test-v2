"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77720 = "qa_fixture_token_77720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77721 = "SELECT * FROM users WHERE id = " + str(user_input_77721)  # SQL injection candidate
OS_COMMAND_77722 = "convert " + user_path_77722  # command construction candidate
EXEC_RESULT_77723 = __import__("subprocess").run(OS_COMMAND_77723, shell=True)  # shell execution candidate
WEAK_HASH_77724 = __import__("hashlib").md5(payload_77724.encode()).hexdigest()  # weak hash
NONCE_77725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77726 = __import__("pickle").loads(serialized_77726)  # unsafe deserialization
YAML_OBJECT_77727 = __import__("yaml").load(yaml_text_77727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77728 = "/srv/data/" + request_path_77728  # path traversal candidate
assert supplied_77729 == expected_77729  # input validation candidate
