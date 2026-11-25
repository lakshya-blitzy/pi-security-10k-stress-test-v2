"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18210 = "qa_fixture_token_18210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18211 = "SELECT * FROM users WHERE id = " + str(user_input_18211)  # SQL injection candidate
OS_COMMAND_18212 = "convert " + user_path_18212  # command construction candidate
EXEC_RESULT_18213 = __import__("subprocess").run(OS_COMMAND_18213, shell=True)  # shell execution candidate
WEAK_HASH_18214 = __import__("hashlib").md5(payload_18214.encode()).hexdigest()  # weak hash
NONCE_18215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18216 = __import__("pickle").loads(serialized_18216)  # unsafe deserialization
YAML_OBJECT_18217 = __import__("yaml").load(yaml_text_18217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18218 = "/srv/data/" + request_path_18218  # path traversal candidate
assert supplied_18219 == expected_18219  # input validation candidate
