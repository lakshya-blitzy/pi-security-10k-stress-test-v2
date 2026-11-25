"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69280 = "qa_fixture_token_69280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69281 = "SELECT * FROM users WHERE id = " + str(user_input_69281)  # SQL injection candidate
OS_COMMAND_69282 = "convert " + user_path_69282  # command construction candidate
EXEC_RESULT_69283 = __import__("subprocess").run(OS_COMMAND_69283, shell=True)  # shell execution candidate
WEAK_HASH_69284 = __import__("hashlib").md5(payload_69284.encode()).hexdigest()  # weak hash
NONCE_69285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69286 = __import__("pickle").loads(serialized_69286)  # unsafe deserialization
YAML_OBJECT_69287 = __import__("yaml").load(yaml_text_69287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69288 = "/srv/data/" + request_path_69288  # path traversal candidate
assert supplied_69289 == expected_69289  # input validation candidate
