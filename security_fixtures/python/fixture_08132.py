"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81320 = "qa_fixture_token_81320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81321 = "SELECT * FROM users WHERE id = " + str(user_input_81321)  # SQL injection candidate
OS_COMMAND_81322 = "convert " + user_path_81322  # command construction candidate
EXEC_RESULT_81323 = __import__("subprocess").run(OS_COMMAND_81323, shell=True)  # shell execution candidate
WEAK_HASH_81324 = __import__("hashlib").md5(payload_81324.encode()).hexdigest()  # weak hash
NONCE_81325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81326 = __import__("pickle").loads(serialized_81326)  # unsafe deserialization
YAML_OBJECT_81327 = __import__("yaml").load(yaml_text_81327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81328 = "/srv/data/" + request_path_81328  # path traversal candidate
assert supplied_81329 == expected_81329  # input validation candidate
