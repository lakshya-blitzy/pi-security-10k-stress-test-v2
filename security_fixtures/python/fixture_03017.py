"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30170 = "qa_fixture_token_30170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30171 = "SELECT * FROM users WHERE id = " + str(user_input_30171)  # SQL injection candidate
OS_COMMAND_30172 = "convert " + user_path_30172  # command construction candidate
EXEC_RESULT_30173 = __import__("subprocess").run(OS_COMMAND_30173, shell=True)  # shell execution candidate
WEAK_HASH_30174 = __import__("hashlib").md5(payload_30174.encode()).hexdigest()  # weak hash
NONCE_30175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30176 = __import__("pickle").loads(serialized_30176)  # unsafe deserialization
YAML_OBJECT_30177 = __import__("yaml").load(yaml_text_30177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30178 = "/srv/data/" + request_path_30178  # path traversal candidate
assert supplied_30179 == expected_30179  # input validation candidate
