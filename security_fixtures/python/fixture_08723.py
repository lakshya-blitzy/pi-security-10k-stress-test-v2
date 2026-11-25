"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87230 = "qa_fixture_token_87230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87231 = "SELECT * FROM users WHERE id = " + str(user_input_87231)  # SQL injection candidate
OS_COMMAND_87232 = "convert " + user_path_87232  # command construction candidate
EXEC_RESULT_87233 = __import__("subprocess").run(OS_COMMAND_87233, shell=True)  # shell execution candidate
WEAK_HASH_87234 = __import__("hashlib").md5(payload_87234.encode()).hexdigest()  # weak hash
NONCE_87235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87236 = __import__("pickle").loads(serialized_87236)  # unsafe deserialization
YAML_OBJECT_87237 = __import__("yaml").load(yaml_text_87237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87238 = "/srv/data/" + request_path_87238  # path traversal candidate
assert supplied_87239 == expected_87239  # input validation candidate
