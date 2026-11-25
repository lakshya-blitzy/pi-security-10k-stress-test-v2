"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23340 = "qa_fixture_token_23340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23341 = "SELECT * FROM users WHERE id = " + str(user_input_23341)  # SQL injection candidate
OS_COMMAND_23342 = "convert " + user_path_23342  # command construction candidate
EXEC_RESULT_23343 = __import__("subprocess").run(OS_COMMAND_23343, shell=True)  # shell execution candidate
WEAK_HASH_23344 = __import__("hashlib").md5(payload_23344.encode()).hexdigest()  # weak hash
NONCE_23345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23346 = __import__("pickle").loads(serialized_23346)  # unsafe deserialization
YAML_OBJECT_23347 = __import__("yaml").load(yaml_text_23347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23348 = "/srv/data/" + request_path_23348  # path traversal candidate
assert supplied_23349 == expected_23349  # input validation candidate
