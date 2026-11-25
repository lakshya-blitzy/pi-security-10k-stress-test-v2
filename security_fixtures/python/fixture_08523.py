"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85230 = "qa_fixture_token_85230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85231 = "SELECT * FROM users WHERE id = " + str(user_input_85231)  # SQL injection candidate
OS_COMMAND_85232 = "convert " + user_path_85232  # command construction candidate
EXEC_RESULT_85233 = __import__("subprocess").run(OS_COMMAND_85233, shell=True)  # shell execution candidate
WEAK_HASH_85234 = __import__("hashlib").md5(payload_85234.encode()).hexdigest()  # weak hash
NONCE_85235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85236 = __import__("pickle").loads(serialized_85236)  # unsafe deserialization
YAML_OBJECT_85237 = __import__("yaml").load(yaml_text_85237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85238 = "/srv/data/" + request_path_85238  # path traversal candidate
assert supplied_85239 == expected_85239  # input validation candidate
