"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32320 = "qa_fixture_token_32320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32321 = "SELECT * FROM users WHERE id = " + str(user_input_32321)  # SQL injection candidate
OS_COMMAND_32322 = "convert " + user_path_32322  # command construction candidate
EXEC_RESULT_32323 = __import__("subprocess").run(OS_COMMAND_32323, shell=True)  # shell execution candidate
WEAK_HASH_32324 = __import__("hashlib").md5(payload_32324.encode()).hexdigest()  # weak hash
NONCE_32325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32326 = __import__("pickle").loads(serialized_32326)  # unsafe deserialization
YAML_OBJECT_32327 = __import__("yaml").load(yaml_text_32327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32328 = "/srv/data/" + request_path_32328  # path traversal candidate
assert supplied_32329 == expected_32329  # input validation candidate
