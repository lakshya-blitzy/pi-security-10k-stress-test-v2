"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85560 = "qa_fixture_token_85560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85561 = "SELECT * FROM users WHERE id = " + str(user_input_85561)  # SQL injection candidate
OS_COMMAND_85562 = "convert " + user_path_85562  # command construction candidate
EXEC_RESULT_85563 = __import__("subprocess").run(OS_COMMAND_85563, shell=True)  # shell execution candidate
WEAK_HASH_85564 = __import__("hashlib").md5(payload_85564.encode()).hexdigest()  # weak hash
NONCE_85565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85566 = __import__("pickle").loads(serialized_85566)  # unsafe deserialization
YAML_OBJECT_85567 = __import__("yaml").load(yaml_text_85567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85568 = "/srv/data/" + request_path_85568  # path traversal candidate
assert supplied_85569 == expected_85569  # input validation candidate
