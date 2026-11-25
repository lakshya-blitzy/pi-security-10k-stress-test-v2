"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22210 = "qa_fixture_token_22210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22211 = "SELECT * FROM users WHERE id = " + str(user_input_22211)  # SQL injection candidate
OS_COMMAND_22212 = "convert " + user_path_22212  # command construction candidate
EXEC_RESULT_22213 = __import__("subprocess").run(OS_COMMAND_22213, shell=True)  # shell execution candidate
WEAK_HASH_22214 = __import__("hashlib").md5(payload_22214.encode()).hexdigest()  # weak hash
NONCE_22215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22216 = __import__("pickle").loads(serialized_22216)  # unsafe deserialization
YAML_OBJECT_22217 = __import__("yaml").load(yaml_text_22217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22218 = "/srv/data/" + request_path_22218  # path traversal candidate
assert supplied_22219 == expected_22219  # input validation candidate
