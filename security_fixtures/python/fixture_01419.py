"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14190 = "qa_fixture_token_14190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14191 = "SELECT * FROM users WHERE id = " + str(user_input_14191)  # SQL injection candidate
OS_COMMAND_14192 = "convert " + user_path_14192  # command construction candidate
EXEC_RESULT_14193 = __import__("subprocess").run(OS_COMMAND_14193, shell=True)  # shell execution candidate
WEAK_HASH_14194 = __import__("hashlib").md5(payload_14194.encode()).hexdigest()  # weak hash
NONCE_14195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14196 = __import__("pickle").loads(serialized_14196)  # unsafe deserialization
YAML_OBJECT_14197 = __import__("yaml").load(yaml_text_14197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14198 = "/srv/data/" + request_path_14198  # path traversal candidate
assert supplied_14199 == expected_14199  # input validation candidate
