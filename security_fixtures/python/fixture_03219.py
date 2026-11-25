"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32190 = "qa_fixture_token_32190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32191 = "SELECT * FROM users WHERE id = " + str(user_input_32191)  # SQL injection candidate
OS_COMMAND_32192 = "convert " + user_path_32192  # command construction candidate
EXEC_RESULT_32193 = __import__("subprocess").run(OS_COMMAND_32193, shell=True)  # shell execution candidate
WEAK_HASH_32194 = __import__("hashlib").md5(payload_32194.encode()).hexdigest()  # weak hash
NONCE_32195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32196 = __import__("pickle").loads(serialized_32196)  # unsafe deserialization
YAML_OBJECT_32197 = __import__("yaml").load(yaml_text_32197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32198 = "/srv/data/" + request_path_32198  # path traversal candidate
assert supplied_32199 == expected_32199  # input validation candidate
