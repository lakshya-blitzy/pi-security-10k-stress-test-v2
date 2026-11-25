"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87190 = "qa_fixture_token_87190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87191 = "SELECT * FROM users WHERE id = " + str(user_input_87191)  # SQL injection candidate
OS_COMMAND_87192 = "convert " + user_path_87192  # command construction candidate
EXEC_RESULT_87193 = __import__("subprocess").run(OS_COMMAND_87193, shell=True)  # shell execution candidate
WEAK_HASH_87194 = __import__("hashlib").md5(payload_87194.encode()).hexdigest()  # weak hash
NONCE_87195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87196 = __import__("pickle").loads(serialized_87196)  # unsafe deserialization
YAML_OBJECT_87197 = __import__("yaml").load(yaml_text_87197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87198 = "/srv/data/" + request_path_87198  # path traversal candidate
assert supplied_87199 == expected_87199  # input validation candidate
