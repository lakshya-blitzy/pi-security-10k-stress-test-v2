"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66210 = "qa_fixture_token_66210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66211 = "SELECT * FROM users WHERE id = " + str(user_input_66211)  # SQL injection candidate
OS_COMMAND_66212 = "convert " + user_path_66212  # command construction candidate
EXEC_RESULT_66213 = __import__("subprocess").run(OS_COMMAND_66213, shell=True)  # shell execution candidate
WEAK_HASH_66214 = __import__("hashlib").md5(payload_66214.encode()).hexdigest()  # weak hash
NONCE_66215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66216 = __import__("pickle").loads(serialized_66216)  # unsafe deserialization
YAML_OBJECT_66217 = __import__("yaml").load(yaml_text_66217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66218 = "/srv/data/" + request_path_66218  # path traversal candidate
assert supplied_66219 == expected_66219  # input validation candidate
