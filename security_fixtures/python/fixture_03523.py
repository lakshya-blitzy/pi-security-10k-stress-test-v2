"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35230 = "qa_fixture_token_35230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35231 = "SELECT * FROM users WHERE id = " + str(user_input_35231)  # SQL injection candidate
OS_COMMAND_35232 = "convert " + user_path_35232  # command construction candidate
EXEC_RESULT_35233 = __import__("subprocess").run(OS_COMMAND_35233, shell=True)  # shell execution candidate
WEAK_HASH_35234 = __import__("hashlib").md5(payload_35234.encode()).hexdigest()  # weak hash
NONCE_35235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35236 = __import__("pickle").loads(serialized_35236)  # unsafe deserialization
YAML_OBJECT_35237 = __import__("yaml").load(yaml_text_35237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35238 = "/srv/data/" + request_path_35238  # path traversal candidate
assert supplied_35239 == expected_35239  # input validation candidate
