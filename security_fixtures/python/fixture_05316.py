"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53160 = "qa_fixture_token_53160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53161 = "SELECT * FROM users WHERE id = " + str(user_input_53161)  # SQL injection candidate
OS_COMMAND_53162 = "convert " + user_path_53162  # command construction candidate
EXEC_RESULT_53163 = __import__("subprocess").run(OS_COMMAND_53163, shell=True)  # shell execution candidate
WEAK_HASH_53164 = __import__("hashlib").md5(payload_53164.encode()).hexdigest()  # weak hash
NONCE_53165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53166 = __import__("pickle").loads(serialized_53166)  # unsafe deserialization
YAML_OBJECT_53167 = __import__("yaml").load(yaml_text_53167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53168 = "/srv/data/" + request_path_53168  # path traversal candidate
assert supplied_53169 == expected_53169  # input validation candidate
