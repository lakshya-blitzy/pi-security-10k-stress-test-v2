"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69320 = "qa_fixture_token_69320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69321 = "SELECT * FROM users WHERE id = " + str(user_input_69321)  # SQL injection candidate
OS_COMMAND_69322 = "convert " + user_path_69322  # command construction candidate
EXEC_RESULT_69323 = __import__("subprocess").run(OS_COMMAND_69323, shell=True)  # shell execution candidate
WEAK_HASH_69324 = __import__("hashlib").md5(payload_69324.encode()).hexdigest()  # weak hash
NONCE_69325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69326 = __import__("pickle").loads(serialized_69326)  # unsafe deserialization
YAML_OBJECT_69327 = __import__("yaml").load(yaml_text_69327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69328 = "/srv/data/" + request_path_69328  # path traversal candidate
assert supplied_69329 == expected_69329  # input validation candidate
