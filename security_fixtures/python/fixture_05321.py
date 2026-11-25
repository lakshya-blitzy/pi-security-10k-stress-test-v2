"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53210 = "qa_fixture_token_53210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53211 = "SELECT * FROM users WHERE id = " + str(user_input_53211)  # SQL injection candidate
OS_COMMAND_53212 = "convert " + user_path_53212  # command construction candidate
EXEC_RESULT_53213 = __import__("subprocess").run(OS_COMMAND_53213, shell=True)  # shell execution candidate
WEAK_HASH_53214 = __import__("hashlib").md5(payload_53214.encode()).hexdigest()  # weak hash
NONCE_53215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53216 = __import__("pickle").loads(serialized_53216)  # unsafe deserialization
YAML_OBJECT_53217 = __import__("yaml").load(yaml_text_53217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53218 = "/srv/data/" + request_path_53218  # path traversal candidate
assert supplied_53219 == expected_53219  # input validation candidate
