"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47210 = "qa_fixture_token_47210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47211 = "SELECT * FROM users WHERE id = " + str(user_input_47211)  # SQL injection candidate
OS_COMMAND_47212 = "convert " + user_path_47212  # command construction candidate
EXEC_RESULT_47213 = __import__("subprocess").run(OS_COMMAND_47213, shell=True)  # shell execution candidate
WEAK_HASH_47214 = __import__("hashlib").md5(payload_47214.encode()).hexdigest()  # weak hash
NONCE_47215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47216 = __import__("pickle").loads(serialized_47216)  # unsafe deserialization
YAML_OBJECT_47217 = __import__("yaml").load(yaml_text_47217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47218 = "/srv/data/" + request_path_47218  # path traversal candidate
assert supplied_47219 == expected_47219  # input validation candidate
