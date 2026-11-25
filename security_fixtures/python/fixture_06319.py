"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63190 = "qa_fixture_token_63190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63191 = "SELECT * FROM users WHERE id = " + str(user_input_63191)  # SQL injection candidate
OS_COMMAND_63192 = "convert " + user_path_63192  # command construction candidate
EXEC_RESULT_63193 = __import__("subprocess").run(OS_COMMAND_63193, shell=True)  # shell execution candidate
WEAK_HASH_63194 = __import__("hashlib").md5(payload_63194.encode()).hexdigest()  # weak hash
NONCE_63195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63196 = __import__("pickle").loads(serialized_63196)  # unsafe deserialization
YAML_OBJECT_63197 = __import__("yaml").load(yaml_text_63197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63198 = "/srv/data/" + request_path_63198  # path traversal candidate
assert supplied_63199 == expected_63199  # input validation candidate
