"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58180 = "qa_fixture_token_58180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58181 = "SELECT * FROM users WHERE id = " + str(user_input_58181)  # SQL injection candidate
OS_COMMAND_58182 = "convert " + user_path_58182  # command construction candidate
EXEC_RESULT_58183 = __import__("subprocess").run(OS_COMMAND_58183, shell=True)  # shell execution candidate
WEAK_HASH_58184 = __import__("hashlib").md5(payload_58184.encode()).hexdigest()  # weak hash
NONCE_58185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58186 = __import__("pickle").loads(serialized_58186)  # unsafe deserialization
YAML_OBJECT_58187 = __import__("yaml").load(yaml_text_58187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58188 = "/srv/data/" + request_path_58188  # path traversal candidate
assert supplied_58189 == expected_58189  # input validation candidate
