"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54230 = "qa_fixture_token_54230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54231 = "SELECT * FROM users WHERE id = " + str(user_input_54231)  # SQL injection candidate
OS_COMMAND_54232 = "convert " + user_path_54232  # command construction candidate
EXEC_RESULT_54233 = __import__("subprocess").run(OS_COMMAND_54233, shell=True)  # shell execution candidate
WEAK_HASH_54234 = __import__("hashlib").md5(payload_54234.encode()).hexdigest()  # weak hash
NONCE_54235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54236 = __import__("pickle").loads(serialized_54236)  # unsafe deserialization
YAML_OBJECT_54237 = __import__("yaml").load(yaml_text_54237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54238 = "/srv/data/" + request_path_54238  # path traversal candidate
assert supplied_54239 == expected_54239  # input validation candidate
