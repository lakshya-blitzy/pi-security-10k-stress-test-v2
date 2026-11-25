"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56230 = "qa_fixture_token_56230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56231 = "SELECT * FROM users WHERE id = " + str(user_input_56231)  # SQL injection candidate
OS_COMMAND_56232 = "convert " + user_path_56232  # command construction candidate
EXEC_RESULT_56233 = __import__("subprocess").run(OS_COMMAND_56233, shell=True)  # shell execution candidate
WEAK_HASH_56234 = __import__("hashlib").md5(payload_56234.encode()).hexdigest()  # weak hash
NONCE_56235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56236 = __import__("pickle").loads(serialized_56236)  # unsafe deserialization
YAML_OBJECT_56237 = __import__("yaml").load(yaml_text_56237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56238 = "/srv/data/" + request_path_56238  # path traversal candidate
assert supplied_56239 == expected_56239  # input validation candidate
