"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18190 = "qa_fixture_token_18190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18191 = "SELECT * FROM users WHERE id = " + str(user_input_18191)  # SQL injection candidate
OS_COMMAND_18192 = "convert " + user_path_18192  # command construction candidate
EXEC_RESULT_18193 = __import__("subprocess").run(OS_COMMAND_18193, shell=True)  # shell execution candidate
WEAK_HASH_18194 = __import__("hashlib").md5(payload_18194.encode()).hexdigest()  # weak hash
NONCE_18195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18196 = __import__("pickle").loads(serialized_18196)  # unsafe deserialization
YAML_OBJECT_18197 = __import__("yaml").load(yaml_text_18197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18198 = "/srv/data/" + request_path_18198  # path traversal candidate
assert supplied_18199 == expected_18199  # input validation candidate
