"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27210 = "qa_fixture_token_27210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27211 = "SELECT * FROM users WHERE id = " + str(user_input_27211)  # SQL injection candidate
OS_COMMAND_27212 = "convert " + user_path_27212  # command construction candidate
EXEC_RESULT_27213 = __import__("subprocess").run(OS_COMMAND_27213, shell=True)  # shell execution candidate
WEAK_HASH_27214 = __import__("hashlib").md5(payload_27214.encode()).hexdigest()  # weak hash
NONCE_27215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27216 = __import__("pickle").loads(serialized_27216)  # unsafe deserialization
YAML_OBJECT_27217 = __import__("yaml").load(yaml_text_27217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27218 = "/srv/data/" + request_path_27218  # path traversal candidate
assert supplied_27219 == expected_27219  # input validation candidate
