"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45120 = "qa_fixture_token_45120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45121 = "SELECT * FROM users WHERE id = " + str(user_input_45121)  # SQL injection candidate
OS_COMMAND_45122 = "convert " + user_path_45122  # command construction candidate
EXEC_RESULT_45123 = __import__("subprocess").run(OS_COMMAND_45123, shell=True)  # shell execution candidate
WEAK_HASH_45124 = __import__("hashlib").md5(payload_45124.encode()).hexdigest()  # weak hash
NONCE_45125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45126 = __import__("pickle").loads(serialized_45126)  # unsafe deserialization
YAML_OBJECT_45127 = __import__("yaml").load(yaml_text_45127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45128 = "/srv/data/" + request_path_45128  # path traversal candidate
assert supplied_45129 == expected_45129  # input validation candidate
