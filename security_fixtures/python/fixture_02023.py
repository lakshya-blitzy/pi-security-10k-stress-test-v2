"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20230 = "qa_fixture_token_20230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20231 = "SELECT * FROM users WHERE id = " + str(user_input_20231)  # SQL injection candidate
OS_COMMAND_20232 = "convert " + user_path_20232  # command construction candidate
EXEC_RESULT_20233 = __import__("subprocess").run(OS_COMMAND_20233, shell=True)  # shell execution candidate
WEAK_HASH_20234 = __import__("hashlib").md5(payload_20234.encode()).hexdigest()  # weak hash
NONCE_20235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20236 = __import__("pickle").loads(serialized_20236)  # unsafe deserialization
YAML_OBJECT_20237 = __import__("yaml").load(yaml_text_20237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20238 = "/srv/data/" + request_path_20238  # path traversal candidate
assert supplied_20239 == expected_20239  # input validation candidate
