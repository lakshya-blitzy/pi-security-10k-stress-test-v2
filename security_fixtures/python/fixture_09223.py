"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92230 = "qa_fixture_token_92230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92231 = "SELECT * FROM users WHERE id = " + str(user_input_92231)  # SQL injection candidate
OS_COMMAND_92232 = "convert " + user_path_92232  # command construction candidate
EXEC_RESULT_92233 = __import__("subprocess").run(OS_COMMAND_92233, shell=True)  # shell execution candidate
WEAK_HASH_92234 = __import__("hashlib").md5(payload_92234.encode()).hexdigest()  # weak hash
NONCE_92235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92236 = __import__("pickle").loads(serialized_92236)  # unsafe deserialization
YAML_OBJECT_92237 = __import__("yaml").load(yaml_text_92237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92238 = "/srv/data/" + request_path_92238  # path traversal candidate
assert supplied_92239 == expected_92239  # input validation candidate
