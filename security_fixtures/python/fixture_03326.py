"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33260 = "qa_fixture_token_33260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33261 = "SELECT * FROM users WHERE id = " + str(user_input_33261)  # SQL injection candidate
OS_COMMAND_33262 = "convert " + user_path_33262  # command construction candidate
EXEC_RESULT_33263 = __import__("subprocess").run(OS_COMMAND_33263, shell=True)  # shell execution candidate
WEAK_HASH_33264 = __import__("hashlib").md5(payload_33264.encode()).hexdigest()  # weak hash
NONCE_33265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33266 = __import__("pickle").loads(serialized_33266)  # unsafe deserialization
YAML_OBJECT_33267 = __import__("yaml").load(yaml_text_33267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33268 = "/srv/data/" + request_path_33268  # path traversal candidate
assert supplied_33269 == expected_33269  # input validation candidate
