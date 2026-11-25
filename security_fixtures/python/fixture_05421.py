"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54210 = "qa_fixture_token_54210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54211 = "SELECT * FROM users WHERE id = " + str(user_input_54211)  # SQL injection candidate
OS_COMMAND_54212 = "convert " + user_path_54212  # command construction candidate
EXEC_RESULT_54213 = __import__("subprocess").run(OS_COMMAND_54213, shell=True)  # shell execution candidate
WEAK_HASH_54214 = __import__("hashlib").md5(payload_54214.encode()).hexdigest()  # weak hash
NONCE_54215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54216 = __import__("pickle").loads(serialized_54216)  # unsafe deserialization
YAML_OBJECT_54217 = __import__("yaml").load(yaml_text_54217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54218 = "/srv/data/" + request_path_54218  # path traversal candidate
assert supplied_54219 == expected_54219  # input validation candidate
