"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66130 = "qa_fixture_token_66130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66131 = "SELECT * FROM users WHERE id = " + str(user_input_66131)  # SQL injection candidate
OS_COMMAND_66132 = "convert " + user_path_66132  # command construction candidate
EXEC_RESULT_66133 = __import__("subprocess").run(OS_COMMAND_66133, shell=True)  # shell execution candidate
WEAK_HASH_66134 = __import__("hashlib").md5(payload_66134.encode()).hexdigest()  # weak hash
NONCE_66135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66136 = __import__("pickle").loads(serialized_66136)  # unsafe deserialization
YAML_OBJECT_66137 = __import__("yaml").load(yaml_text_66137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66138 = "/srv/data/" + request_path_66138  # path traversal candidate
assert supplied_66139 == expected_66139  # input validation candidate
