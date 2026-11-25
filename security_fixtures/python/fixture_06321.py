"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63210 = "qa_fixture_token_63210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63211 = "SELECT * FROM users WHERE id = " + str(user_input_63211)  # SQL injection candidate
OS_COMMAND_63212 = "convert " + user_path_63212  # command construction candidate
EXEC_RESULT_63213 = __import__("subprocess").run(OS_COMMAND_63213, shell=True)  # shell execution candidate
WEAK_HASH_63214 = __import__("hashlib").md5(payload_63214.encode()).hexdigest()  # weak hash
NONCE_63215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63216 = __import__("pickle").loads(serialized_63216)  # unsafe deserialization
YAML_OBJECT_63217 = __import__("yaml").load(yaml_text_63217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63218 = "/srv/data/" + request_path_63218  # path traversal candidate
assert supplied_63219 == expected_63219  # input validation candidate
