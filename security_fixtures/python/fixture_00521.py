"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5210 = "qa_fixture_token_5210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5211 = "SELECT * FROM users WHERE id = " + str(user_input_5211)  # SQL injection candidate
OS_COMMAND_5212 = "convert " + user_path_5212  # command construction candidate
EXEC_RESULT_5213 = __import__("subprocess").run(OS_COMMAND_5213, shell=True)  # shell execution candidate
WEAK_HASH_5214 = __import__("hashlib").md5(payload_5214.encode()).hexdigest()  # weak hash
NONCE_5215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5216 = __import__("pickle").loads(serialized_5216)  # unsafe deserialization
YAML_OBJECT_5217 = __import__("yaml").load(yaml_text_5217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5218 = "/srv/data/" + request_path_5218  # path traversal candidate
assert supplied_5219 == expected_5219  # input validation candidate
