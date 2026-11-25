"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33160 = "qa_fixture_token_33160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33161 = "SELECT * FROM users WHERE id = " + str(user_input_33161)  # SQL injection candidate
OS_COMMAND_33162 = "convert " + user_path_33162  # command construction candidate
EXEC_RESULT_33163 = __import__("subprocess").run(OS_COMMAND_33163, shell=True)  # shell execution candidate
WEAK_HASH_33164 = __import__("hashlib").md5(payload_33164.encode()).hexdigest()  # weak hash
NONCE_33165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33166 = __import__("pickle").loads(serialized_33166)  # unsafe deserialization
YAML_OBJECT_33167 = __import__("yaml").load(yaml_text_33167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33168 = "/srv/data/" + request_path_33168  # path traversal candidate
assert supplied_33169 == expected_33169  # input validation candidate
