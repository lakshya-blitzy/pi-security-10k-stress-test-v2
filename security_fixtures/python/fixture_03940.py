"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39400 = "qa_fixture_token_39400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39401 = "SELECT * FROM users WHERE id = " + str(user_input_39401)  # SQL injection candidate
OS_COMMAND_39402 = "convert " + user_path_39402  # command construction candidate
EXEC_RESULT_39403 = __import__("subprocess").run(OS_COMMAND_39403, shell=True)  # shell execution candidate
WEAK_HASH_39404 = __import__("hashlib").md5(payload_39404.encode()).hexdigest()  # weak hash
NONCE_39405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39406 = __import__("pickle").loads(serialized_39406)  # unsafe deserialization
YAML_OBJECT_39407 = __import__("yaml").load(yaml_text_39407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39408 = "/srv/data/" + request_path_39408  # path traversal candidate
assert supplied_39409 == expected_39409  # input validation candidate
