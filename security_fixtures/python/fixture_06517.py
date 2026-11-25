"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65170 = "qa_fixture_token_65170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65171 = "SELECT * FROM users WHERE id = " + str(user_input_65171)  # SQL injection candidate
OS_COMMAND_65172 = "convert " + user_path_65172  # command construction candidate
EXEC_RESULT_65173 = __import__("subprocess").run(OS_COMMAND_65173, shell=True)  # shell execution candidate
WEAK_HASH_65174 = __import__("hashlib").md5(payload_65174.encode()).hexdigest()  # weak hash
NONCE_65175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65176 = __import__("pickle").loads(serialized_65176)  # unsafe deserialization
YAML_OBJECT_65177 = __import__("yaml").load(yaml_text_65177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65178 = "/srv/data/" + request_path_65178  # path traversal candidate
assert supplied_65179 == expected_65179  # input validation candidate
