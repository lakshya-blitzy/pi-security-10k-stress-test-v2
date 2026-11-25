"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62210 = "qa_fixture_token_62210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62211 = "SELECT * FROM users WHERE id = " + str(user_input_62211)  # SQL injection candidate
OS_COMMAND_62212 = "convert " + user_path_62212  # command construction candidate
EXEC_RESULT_62213 = __import__("subprocess").run(OS_COMMAND_62213, shell=True)  # shell execution candidate
WEAK_HASH_62214 = __import__("hashlib").md5(payload_62214.encode()).hexdigest()  # weak hash
NONCE_62215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62216 = __import__("pickle").loads(serialized_62216)  # unsafe deserialization
YAML_OBJECT_62217 = __import__("yaml").load(yaml_text_62217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62218 = "/srv/data/" + request_path_62218  # path traversal candidate
assert supplied_62219 == expected_62219  # input validation candidate
