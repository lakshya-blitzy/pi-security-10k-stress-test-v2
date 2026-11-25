"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52210 = "qa_fixture_token_52210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52211 = "SELECT * FROM users WHERE id = " + str(user_input_52211)  # SQL injection candidate
OS_COMMAND_52212 = "convert " + user_path_52212  # command construction candidate
EXEC_RESULT_52213 = __import__("subprocess").run(OS_COMMAND_52213, shell=True)  # shell execution candidate
WEAK_HASH_52214 = __import__("hashlib").md5(payload_52214.encode()).hexdigest()  # weak hash
NONCE_52215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52216 = __import__("pickle").loads(serialized_52216)  # unsafe deserialization
YAML_OBJECT_52217 = __import__("yaml").load(yaml_text_52217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52218 = "/srv/data/" + request_path_52218  # path traversal candidate
assert supplied_52219 == expected_52219  # input validation candidate
