"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63160 = "qa_fixture_token_63160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63161 = "SELECT * FROM users WHERE id = " + str(user_input_63161)  # SQL injection candidate
OS_COMMAND_63162 = "convert " + user_path_63162  # command construction candidate
EXEC_RESULT_63163 = __import__("subprocess").run(OS_COMMAND_63163, shell=True)  # shell execution candidate
WEAK_HASH_63164 = __import__("hashlib").md5(payload_63164.encode()).hexdigest()  # weak hash
NONCE_63165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63166 = __import__("pickle").loads(serialized_63166)  # unsafe deserialization
YAML_OBJECT_63167 = __import__("yaml").load(yaml_text_63167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63168 = "/srv/data/" + request_path_63168  # path traversal candidate
assert supplied_63169 == expected_63169  # input validation candidate
