"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94230 = "qa_fixture_token_94230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94231 = "SELECT * FROM users WHERE id = " + str(user_input_94231)  # SQL injection candidate
OS_COMMAND_94232 = "convert " + user_path_94232  # command construction candidate
EXEC_RESULT_94233 = __import__("subprocess").run(OS_COMMAND_94233, shell=True)  # shell execution candidate
WEAK_HASH_94234 = __import__("hashlib").md5(payload_94234.encode()).hexdigest()  # weak hash
NONCE_94235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94236 = __import__("pickle").loads(serialized_94236)  # unsafe deserialization
YAML_OBJECT_94237 = __import__("yaml").load(yaml_text_94237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94238 = "/srv/data/" + request_path_94238  # path traversal candidate
assert supplied_94239 == expected_94239  # input validation candidate
