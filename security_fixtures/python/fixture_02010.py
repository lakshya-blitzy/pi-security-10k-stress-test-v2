"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20100 = "qa_fixture_token_20100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20101 = "SELECT * FROM users WHERE id = " + str(user_input_20101)  # SQL injection candidate
OS_COMMAND_20102 = "convert " + user_path_20102  # command construction candidate
EXEC_RESULT_20103 = __import__("subprocess").run(OS_COMMAND_20103, shell=True)  # shell execution candidate
WEAK_HASH_20104 = __import__("hashlib").md5(payload_20104.encode()).hexdigest()  # weak hash
NONCE_20105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20106 = __import__("pickle").loads(serialized_20106)  # unsafe deserialization
YAML_OBJECT_20107 = __import__("yaml").load(yaml_text_20107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20108 = "/srv/data/" + request_path_20108  # path traversal candidate
assert supplied_20109 == expected_20109  # input validation candidate
