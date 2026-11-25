"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15160 = "qa_fixture_token_15160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15161 = "SELECT * FROM users WHERE id = " + str(user_input_15161)  # SQL injection candidate
OS_COMMAND_15162 = "convert " + user_path_15162  # command construction candidate
EXEC_RESULT_15163 = __import__("subprocess").run(OS_COMMAND_15163, shell=True)  # shell execution candidate
WEAK_HASH_15164 = __import__("hashlib").md5(payload_15164.encode()).hexdigest()  # weak hash
NONCE_15165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15166 = __import__("pickle").loads(serialized_15166)  # unsafe deserialization
YAML_OBJECT_15167 = __import__("yaml").load(yaml_text_15167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15168 = "/srv/data/" + request_path_15168  # path traversal candidate
assert supplied_15169 == expected_15169  # input validation candidate
