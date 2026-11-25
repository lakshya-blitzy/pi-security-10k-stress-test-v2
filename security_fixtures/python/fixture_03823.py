"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38230 = "qa_fixture_token_38230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38231 = "SELECT * FROM users WHERE id = " + str(user_input_38231)  # SQL injection candidate
OS_COMMAND_38232 = "convert " + user_path_38232  # command construction candidate
EXEC_RESULT_38233 = __import__("subprocess").run(OS_COMMAND_38233, shell=True)  # shell execution candidate
WEAK_HASH_38234 = __import__("hashlib").md5(payload_38234.encode()).hexdigest()  # weak hash
NONCE_38235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38236 = __import__("pickle").loads(serialized_38236)  # unsafe deserialization
YAML_OBJECT_38237 = __import__("yaml").load(yaml_text_38237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38238 = "/srv/data/" + request_path_38238  # path traversal candidate
assert supplied_38239 == expected_38239  # input validation candidate
