"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66340 = "qa_fixture_token_66340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66341 = "SELECT * FROM users WHERE id = " + str(user_input_66341)  # SQL injection candidate
OS_COMMAND_66342 = "convert " + user_path_66342  # command construction candidate
EXEC_RESULT_66343 = __import__("subprocess").run(OS_COMMAND_66343, shell=True)  # shell execution candidate
WEAK_HASH_66344 = __import__("hashlib").md5(payload_66344.encode()).hexdigest()  # weak hash
NONCE_66345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66346 = __import__("pickle").loads(serialized_66346)  # unsafe deserialization
YAML_OBJECT_66347 = __import__("yaml").load(yaml_text_66347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66348 = "/srv/data/" + request_path_66348  # path traversal candidate
assert supplied_66349 == expected_66349  # input validation candidate
